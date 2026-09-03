import uuid
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class Loan(models.Model):

    LOAN_TYPES = [
        ("home", "Home"),
        ("car" , "Car"),
        ("bike" , "Bike"),
        ("personal" , "Personal"),
        ("education" , "Education"),
        ("credit_card" , "Credit Card EMI"),
        ("others" , "Others")
    ]

    STATUS_CHOICES = [
        ("pending" , "Pending"),
        ("paid" , "Paid"),
        ("overdue" , "Overdue")
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="transactions")
    loan_name = models.CharField(max_length=120)
    loan_type = models.CharField(max_length=20, choices=LOAN_TYPES)
    principal_amount = models.DecimalField(max_digits=12, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2, help_text="Anual Interest Rate (%)")
    tenure_months = models.PositiveIntegerField()
    emi_amount = models.DecimalField(max_digits=12, decimal_places=2)
    start_date = models.DateField(default=timezone.localdate)
    end_date = models.DateField(default=timezone.localdate)
    outstanding_amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")

    def __str__(self):
        return f"{self.loan_name} - {self.user}"

class EMIPayment(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE, related_name="payments")
    installment_number = models.PositiveIntegerField()
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    principal_component = models.DecimalField(max_digits=12, decimal_places=2)
    interest_component = models.DecimalField(max_digits=12, decimal_places=2)
    paid_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=[("pending", "Pending"), ("paid", "Paid"), ("overdue", "Overdue")], default="pending")

class Transaction(models.Model):
    INCOME = "income"
    EXPENSE = "expense"

    TYPE_CHOICES = [
        (INCOME, "Income"),
        (EXPENSE, "Expense"),
    ]

    INCOME_CATEGORY_CHOICES = [
            ("salary", "Salary"),
            ("freelance", "Freelance"),
            ("business", "Business"),
        ]

    EXPENSE_CATEGORY_CHOICES = [
        ("investment", "Investment"),
        ("food", "Food"),
        ("transport", "Transport"),
        ("shopping", "Shopping"),
        ("rent", "Rent"),
        ("utilities", "Utilities"),
        ("health", "Health"),
        ("education", "Education"),
        ("entertainment", "Entertainment"),
        ("subscriptions", "Subscriptions"),
        ("bills", "Bills"),
        ("travel", "Travel"),
        ("family", "Family"),
        ("other", "Other"),
    ]

    CATEGORY_CHOICES = [
        ("salary", "Salary"),
        ("freelance", "Freelance"),
        ("business", "Business"),
        ("investment", "Investment"),
        ("food", "Food"),
        ("transport", "Transport"),
        ("shopping", "Shopping"),
        ("rent", "Rent"),
        ("utilities", "Utilities"),
        ("health", "Health"),
        ("education", "Education"),
        ("entertainment", "Entertainment"),
        ("subscriptions", "Subscriptions"),
        ("bills", "Bills"),
        ("travel", "Travel"),
        ("family", "Family"),
        ("other", "Other"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="transactions")
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateField(default=timezone.localdate)

    class Meta:
        ordering = ["-date", "-id"]

    def __str__(self):
        return self.name
