from django.contrib import admin
from .models import Paciente, DatosMedicos, Historial


# Register your models here.
@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ['cedula', 'nombre', 'apellido', 'genero', 'fecha_nacimiento']
    list_display_links = ['cedula', 'nombre', 'apellido', 'genero', 'fecha_nacimiento']
    fields = ['cedula', 'nombre', 'apellido', 'fecha_nacimiento', 'direccion', 'genero', 'nacionalidad', 'foto',
              'quien_creo', 'fecha_creacion', 'fecha_actualizacion']
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion')


@admin.register(DatosMedicos)
class DatosMedicosAdmin(admin.ModelAdmin):
    list_display = ['paciente', 'diagnostico', 'doctor_a_cargo', 'estado']
    list_display_links = ['paciente', 'diagnostico', 'doctor_a_cargo']


@admin.register(Historial)
class HistorialAdmin(admin.ModelAdmin):
    list_display = ['paciente', 'tipo_estancia', 'fecha_ingreso', 'fecha_salida', 'condicion']
    list_display_links = ['paciente', 'tipo_estancia', 'fecha_ingreso', 'fecha_salida', 'condicion']