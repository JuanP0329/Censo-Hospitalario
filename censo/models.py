from django.db import models


# Create your models here.
class TipoEstancia(models.Model):
    nombre = models.CharField(max_length=200)
    capacidad = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Tipo estancia"
        verbose_name_plural = "Tipo estancias"

    def __str__(self):
        return f'{self.nombre}'
