from django.db import models
from django.utils.translation import gettext as _


class StayType(models.Model):
    name = models.CharField(max_length=200)
    capacity = models.IntegerField(default=0)

    class Meta:
        verbose_name = _('Stay Type')
        verbose_name_plural = _('Stay Types')
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'
