from django.contrib import admin

from .models import Plan, UrgentMessage


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'stage']


@admin.register(UrgentMessage)
class UrgentMessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'created_at']
