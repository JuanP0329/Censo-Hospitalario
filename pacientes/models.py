from django.db import models
from doctores.models import Doctor

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


class DatosMedicos(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    diagnostico = models.TextField(max_length=200)
    doctor_a_cargo = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    estado = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.paciente.nombre} - {self.paciente.cedula} - {self.doctor_a_cargo}'


class Estancia(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.nombre}'


class Historial(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    estancia = models.ForeignKey(Estancia, on_delete=models.CASCADE)
    fecha_ingreso = models.DateTimeField(null=True)
    fecha_salida = models.DateTimeField(null=True)

    def __str__(self):
        return f'{self.paciente.nombre} - {self.paciente.cedula}'

