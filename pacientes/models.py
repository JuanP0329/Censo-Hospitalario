from django.db import models
from doctores.models import Doctor
from censo.models import TipoEstancia
from django import forms


# Create your models here.
class Auditoria(models.Model):
    quien_creo = models.CharField(max_length=200, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(null=True, auto_now=True)

    class Meta:
        abstract = True


class Paciente(Auditoria):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    cedula = models.IntegerField(primary_key=True)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=200)
    genero = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=100)
    foto = models.ImageField()

    def __str__(self):
        return f'{self.apellido} - {self.nombre}'

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        print('Hola mundo!')
        super().save(force_insert, force_update, using, update_fields)


class DatosMedicos(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    diagnostico = models.TextField(max_length=200)
    doctor_a_cargo = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    estado = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.paciente.nombre} - {self.paciente.cedula} - {self.doctor_a_cargo}'


class Historial(models.Model):
    OPCIONES = [('muerto', 'Muerto'), ('vivo', 'Vivo'), ('en revision', 'En revision')]

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    tipo_estancia = models.ForeignKey(TipoEstancia, on_delete=models.CASCADE)
    fecha_ingreso = models.DateTimeField()
    fecha_salida = models.DateTimeField(blank=True, null=True)
    condicion = models.CharField(max_length=20, choices=OPCIONES, blank=True, null=True)

    def __str__(self):
        return f'{self.paciente.nombre} - {self.paciente.cedula}'


class HistorialForm(forms.ModelForm):
    class Meta:
        model = Historial
        fields = ['condicion']
        widgets = {
            'condicion': forms.RadioSelect
        }
