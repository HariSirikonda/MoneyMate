from django.contrib import admin
from .models import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ("name", "user", "type", "category", "amount", "date")
    list_filter = ("type", "category", "date")
    search_fields = ("name", "description", "user__username")
