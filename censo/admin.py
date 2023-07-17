from django.contrib import admin
from .models import TipoEstancia

# Register your models here.
@admin.register(TipoEstancia)
class TipoEstanciaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'capacidad']
    list_display_links = ['id', 'nombre', 'capacidad']