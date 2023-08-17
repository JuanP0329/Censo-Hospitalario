from django import forms
from django.db import models
from django.utils.translation import gettext as _

from censo.models import StayType
from doctores.models import Doctor


class Auditing(models.Model):
    who_created = models.CharField(max_length=200, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(null=True, auto_now=True)

    class Meta:
        abstract = True


class Patient(Auditing):
    identification = models.IntegerField(primary_key=True)
    photo = models.ImageField(upload_to='pictures', blank=True, null=True)
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_born = models.DateField()
    gender = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    nationality = models.CharField(max_length=100)

    class Meta:
        verbose_name = _('Patient')
        verbose_name_plural = _('Patients')
        ordering = ['identification']

    def __str__(self):
        return f'{self.last_name} - {self.name}'


class MedicalData(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    diagnosis = models.TextField(max_length=200)
    doctor_in_charge = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('Medical Data')
        verbose_name_plural = _('Medical Data')
        ordering = ['patient']

    def __str__(self):
        return f'{self.patient.name} - {self.patient.identification} - {self.doctor_in_charge}'


class MedicalHistory(models.Model):
    OPTIONS = [('dead', _('Dead')), ('live', _('Live')), ('review', _('Under Review'))]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    stay_type = models.ForeignKey(StayType, on_delete=models.CASCADE)
    admission_date = models.DateTimeField()
    date_departure = models.DateTimeField(blank=True, null=True)
    condition = models.CharField(max_length=20, choices=OPTIONS, blank=True, null=True)

    class Meta:
        verbose_name = _('Medical Historial')
        verbose_name_plural = _('Medical Historials')
        ordering = ['patient']

    def __str__(self):
        return f'{self.patient.name} - {self.patient.identification}'


class MedicalHistoryForm(forms.ModelForm):
    class Meta:
        model = MedicalHistory
        fields = ['condition']
        widgets = {
            'condition': forms.RadioSelect
        }
