from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import User

@admin.register(User)
class UserModelAdmin(UserAdmin):
    model = User
    list_display = ["id", "email", "username", "is_staff", "is_active", "is_seller", "is_customer", "is_superuser"]
    list_filter = ["username"]
    fieldsets = (
        ("User Credentials", {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('username', 'city')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_customer', 'is_seller', 'is_superuser')}),
    )
    search_fields = ['email', 'username']
    ordering = ['id'] 
    filter_horizontal = ()  