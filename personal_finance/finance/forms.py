from django import forms
from .models import Transaction, Loan

class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ["name", "type", "principal_amount", "interest_rate", "tenure_months", "emi_amount", "start_date", "end_date", "outstanding_amount", "status"]

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
    def __init__(self, *args, fixed_type=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.fixed_type = fixed_type

        if fixed_type == Transaction.INCOME:
            self.fields["type"].initial = Transaction.INCOME
            self.fields["type"].required = False
            self.fields["category"].choices = Transaction.INCOME_CATEGORY_CHOICES

        elif fixed_type == Transaction.EXPENSE:
            self.fields["type"].initial = Transaction.EXPENSE
            self.fields["type"].required = False
            self.fields["category"].choices = Transaction.EXPENSE_CATEGORY_CHOICES

    def clean_type(self):
        # Since the browser omits the disabled 'type' field from POST,
        # we supply the fixed_type value directly during validation:
        if self.fixed_type:
            return self.fixed_type
        return self.cleaned_data.get("type")
