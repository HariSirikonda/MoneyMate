from django.contrib import admin
from .models import EMIPayment, Transaction, Loan

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ("name", "user", "type", "category", "amount", "date")
    list_filter = ("type", "category", "date")
    search_fields = ("name", "description", "user__username")

@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = (
      "loan_name",
      "user",
      "loan_type",
      "principal_amount",
      "emi_amount",
      "status",
      "start_date",
    )

    list_filter = ("status", "loan_type", "start_date")
    search_fields = ("loan_name", "user__username")
    readonly_fields = ("id",)
    fieldsets = (
        (
          "Basic Information",
          {"fields": ("id", "user", "loan_name", "loan_type", "status")},
        ),
        (
          "Financial Details",
          {
              "fields": (
                  "principal_amount",
                  "interest_rate",
                  "tenure_months",
                  "emi_amount",
                  "outstanding_amount",
              )
          },
        ),
        ("Schedule", {"fields": ("start_date", "end_date")}),
  )

@admin.register(EMIPayment)
class EMIPaymentAdmin(admin.ModelAdmin):
    list_display = (
        "loan",
        "installment_number",
        "amount",
        "principal_component",
        "interest_component",
        "status",
        "paid_date",
    )

    list_filter = ("status", "paid_date", "loan__loan_type")
    search_fields = ("loan__loan_name", "installment_number")
    fieldsets = (
        (
            "Loan & Installment Info",
            {"fields": ("loan", "installment_number", "status")},
        ),
        (
            "Payment Breakdown",
            {"fields": ("amount", "principal_component", "interest_component")},
        ),
        ("Tracking", {"fields": ("paid_date",)}),
    )
