from django.urls import path
from .views import PasswordView, DashboardView

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='seller-dashboard'),
    path('change-password/', PasswordView.as_view(), name='seller-change-password'),
]