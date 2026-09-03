from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("transactions/", views.transactions, name="transactions"),
    path("transactions/add_transaction/", views.add_transaction, name="add_transaction"),
    path("transactions/addIncome/", views.add_income, name="add_income"),
    path("transactions/addExpense/", views.add_expense, name="add_expense"),
    path("transactions/<uuid:pk>/edit/", views.edit_transaction, name="edit_transaction"),
    path("transactions/<uuid:pk>/delete/", views.delete_transaction, name="delete_transaction"),
    path("month/<int:year>/<int:month>/", views.month_detail, name="month_detail"),
    path("loans/", views.loans, name="loans"),
    path("loans/add/",views.add_loan,name="add_loan"),
    path("loans/<uuid:pk>/",views.loan_detail,name="loan_detail"),
    path("emi/<int:pk>/pay/",views.mark_emi_paid,name="mark_emi_paid"),
    path("register/", views.register, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]
