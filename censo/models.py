from django.db import models


# Create your models here.
class Uci(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(max_length=200)
    capacidad = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Uci"
        verbose_name_plural = "Ucis"


class Cama(models.Model):
    tipo = models.CharField(max_length=100)
    estado = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Cama"
        verbose_name_plural = "Camas"


class Ucim(models.Model):
    descripcion = models.TextField(max_length=200)
    capacidad = models.CharField(max_length=100)
    fecha_ingreso = models.DateTimeField()
    fecha_salida = models.DateTimeField()

    class Meta:
        verbose_name = "Ucim"
        verbose_name_plural = "Ucims"


class TipoEstancia(models.Model):
    nombre = models.CharField(max_length=200)
    capacidad = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Tipo estancia"
        verbose_name_plural = "Tipo estancias"

    def __str__(self):
        return f'{self.nombre}'
