from django.urls import path
from customer.views import DashboardView, Passwordview



urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='customer_dashboard'),
    path('password/', Passwordview.as_view(), name='customer_profile'),
]