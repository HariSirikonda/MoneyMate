from calendar import month_name
from datetime import date
from decimal import Decimal
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Sum
from django.shortcuts import get_object_or_404, redirect, render
from .forms import TransactionForm
from .models import Transaction


def _month_summary(user, year, month):
    qs = Transaction.objects.filter(user=user, date__year=year, date__month=month)
    income = qs.filter(type=Transaction.INCOME).aggregate(total=Sum("amount"))["total"] or Decimal("0")
    expense = qs.filter(type=Transaction.EXPENSE).aggregate(total=Sum("amount"))["total"] or Decimal("0")
    savings = income - expense
    savings_rate = (savings / income * 100) if income else Decimal("0")

    category_rows = list(
        qs.filter(type=Transaction.EXPENSE)
        .values("category")
        .annotate(total=Sum("amount"))
        .order_by("-total")
    )
    category_labels = {key: label for key, label in Transaction.CATEGORY_CHOICES}
    for row in category_rows:
        row["label"] = category_labels.get(row["category"], row["category"].title())
        row["percent"] = (row["total"] / expense * 100) if expense else Decimal("0")

    suggestions = []
    if income == 0 and expense > 0:
        suggestions.append("You recorded expenses but no income this month. Review whether all income transactions were entered.")
    if income > 0 and expense > income:
        suggestions.append("Your expenses are higher than your income. Consider reducing non-essential spending.")
    elif income > 0 and savings_rate < 10:
        suggestions.append("Your savings rate is below 10%. Try setting aside a fixed amount immediately after receiving income.")
    elif income > 0 and savings_rate >= 20:
        suggestions.append("Great job! Your savings rate is 20% or higher. Keep protecting that surplus.")
    if category_rows and category_rows[0]["percent"] >= 30:
        suggestions.append(
            f"{category_rows[0]['label']} is your largest expense category at {category_rows[0]['percent']:.1f}% of expenses. "
            "Check if some of this spending can be optimized."
        )
    if qs.count() == 0:
        suggestions.append("No transactions have been recorded for this month yet.")

    return {
        "transactions": qs,
        "income": income,
        "expense": expense,
        "savings": savings,
        "savings_rate": savings_rate,
        "category_rows": category_rows,
        "suggestions": suggestions,
    }


@login_required
def dashboard(request):
    years = set(Transaction.objects.filter(user=request.user).values_list("date__year", flat=True))
    years.add(date.today().year)
    years = sorted(years, reverse=True)

    months = []
    for year in years:
        for month in range(1, 13):
            summary = _month_summary(request.user, year, month)
            months.append({
                "year": year,
                "month": month,
                "name": month_name[month],
                "income": summary["income"],
                "expense": summary["expense"],
                "savings": summary["savings"],
                "has_data": summary["transactions"].exists(),
            })

    return render(request, "finance/dashboard.html", {"months": months, "years": years})


@login_required
def month_detail(request, year, month):
    if month < 1 or month > 12:
        return redirect("dashboard")

    summary = _month_summary(request.user, year, month)
    return render(request, "finance/month_detail.html", {
        **summary,
        "year": year,
        "month": month,
        "month_name": month_name[month],
    })


@login_required
def transactions(request):
    qs = Transaction.objects.filter(user=request.user)
    return render(request, "finance/transactions.html", {"transactions": qs})


@login_required
def add_transaction(request):
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            messages.success(request, "Transaction added successfully.")
            return redirect("transactions")
    else:
        form = TransactionForm()
    return render(request, "finance/transaction_form.html", {"form": form, "title": "Add Transaction"})


@login_required
def edit_transaction(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk, user=request.user)
    if request.method == "POST":
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            messages.success(request, "Transaction updated.")
            return redirect("transactions")
    else:
        form = TransactionForm(instance=transaction)
    return render(request, "finance/transaction_form.html", {"form": form, "title": "Edit Transaction"})


@login_required
def delete_transaction(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk, user=request.user)
    if request.method == "POST":
        transaction.delete()
        messages.success(request, "Transaction deleted.")
        return redirect("transactions")
    return render(request, "finance/delete_confirm.html", {"transaction": transaction})


def register(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dashboard")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {"form": form})
