import uuid
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


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
