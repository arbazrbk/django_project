from django.shortcuts import render
from django.views import View
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import logout
from django.contrib import messages

class Passwordview(PasswordChangeView):
    template_name = 'customer/change_password.html'
    sucess_url = '/dashboard/'
    
    def is_valid(self,form):
        form.save()
        logout(self.request)
        messages.sucess(self.request,"your password has been changed successfully please login again")
        return super().is_valid(form)
    
    def not_valid(self,form):
        messages.error (self.request,"there was an error updating your password")
        return super().not_valid(form)
    
class DashboardView(View):
    def get(self,request,*args,**kwargs):
        return render (request, 'customer/dashboard.html')    