from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ['id', 'email', 'first_name', 'last_name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {
            'fields': (
                'first_name',
                'last_name',
                'middle_name',
                'address',
                'phone_number'
            )
        }),
        ('Permissions', {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
            )
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
