from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=10)
    flag = models.ImageField(upload_to='flags', blank=True, null=True)

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'
        ordering = ['name']

    def __str__(self):
        return self.name
