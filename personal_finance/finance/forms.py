from django import forms
from .models import Transaction


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ["name", "description", "type", "category", "amount", "date"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "e.g. Grocery shopping"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 2, "placeholder": "Optional note"}),
            "type": forms.Select(attrs={"class": "form-select"}),
            "category": forms.Select(attrs={"class": "form-select"}),
            "amount": forms.NumberInput(attrs={"class": "form-control", "placeholder": "0.00", "step": "0.01", "min": "0"}),
            "date": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
        }
