from django.contrib import admin

from .models import StayType


@admin.register(StayType)
class StayTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'capacity']
    list_display_links = list_display
