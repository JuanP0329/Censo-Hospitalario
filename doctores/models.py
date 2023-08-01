from django.db import models


# Create your models here.


class Doctor(models.Model):
    identification = models.IntegerField(primary_key=True)
    photo = models.ImageField(upload_to='pictures', blank=True, null=True)
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    specialty = models.ForeignKey('Specialty', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctores'
        ordering = ['identification']

    def __str__(self):
        return f'{self.name} {self.last_name}'


class Specialty(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Specialty'
        verbose_name_plural = 'Specialties'
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'
