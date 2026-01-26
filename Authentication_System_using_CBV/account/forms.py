from django import forms 
from account.models import User

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','password']
        widgets = {
            
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),           
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'}),
        }