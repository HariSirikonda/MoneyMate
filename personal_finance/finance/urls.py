from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("transactions/", views.transactions, name="transactions"),
    path("transactions/add/", views.add_transaction, name="add_transaction"),
    path("transactions/<uuid:pk>/edit/", views.edit_transaction, name="edit_transaction"),
    path("transactions/<uuid:pk>/delete/", views.delete_transaction, name="delete_transaction"),
    path("month/<int:year>/<int:month>/", views.month_detail, name="month_detail"),
    path("register/", views.register, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]
