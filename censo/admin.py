from django.contrib import admin
from .models import Uci, Cama, Ucim, TipoEstancia

# Register your models here.
@admin.register(Uci)
class UciAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'descripcion', 'capacidad']
    list_display_links = ['id', 'nombre', 'descripcion', 'capacidad']


@admin.register(Cama)
class CamaAdmin(admin.ModelAdmin):
    list_display = ['id', 'tipo', 'estado']
    list_display_links = ['id', 'tipo', 'estado']


@admin.register(Ucim)
class UcimAdmin(admin.ModelAdmin):
    list_display = ['id', 'descripcion', 'capacidad', 'fecha_ingreso', 'fecha_salida']
    list_display_links = ['id', 'descripcion', 'capacidad', 'fecha_ingreso', 'fecha_salida']


@admin.register(TipoEstancia)
class TipoEstanciaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'capacidad']
    list_display_links = ['id', 'nombre', 'capacidad']