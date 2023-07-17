from django.db import models

# Create your models here.


class Doctor(models.Model):
    nombre = models.CharField(max_length=200)
    cedula = models.IntegerField(primary_key=True)
    especialidad = models.CharField(max_length=200)
    correo = models.EmailField(max_length=200)

    def __str__(self):
        return f'{self.nombre}'
