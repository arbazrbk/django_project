from django.shortcuts import render
from django.views import View
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import logout
from django.contrib import messages
from django.urls import reverse_lazy

class DashboardView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'seller/dashboard.html')
    
    
    
class PasswordView(PasswordChangeView):
    template_name = 'seller/change_password.html'
    success_url =  reverse_lazy('login')  
    
    def is_valid(self,form):
        form.save()
        logout(self.request)
        messages.success("the Password is sucessfuly updated")
        return super().is_valid(form)
    
    def not_valid(self,form):
        messages.error("There is something issue while updating pasword of seller")
        return super().not_valid(form)
    
        
    
