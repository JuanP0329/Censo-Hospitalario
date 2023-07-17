from django.contrib import admin
from .models import Doctor

# Register your models here.

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'cedula', 'especialidad', 'correo']
    list_display_links = ['nombre', 'cedula', 'especialidad', 'correo']