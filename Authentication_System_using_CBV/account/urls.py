from django.urls import path 
from account.views import PasswordChangedView, loginView, RegistrationView,HomeView


urlpatterns = [
    path('login/', loginView.as_view(), name='login'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('password-change/', PasswordChangedView.as_view(), name='password_change'),
    path('home/', HomeView.as_view(), name='home'),
]