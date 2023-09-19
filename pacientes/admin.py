from django.contrib import admin
from django.utils.safestring import mark_safe

from .forms import PatientForm
from .models import Patient, MedicalData, MedicalHistory, Comorbidity

class PatientComorbidityInline(admin.StackedInline):
    model = Comorbidity
    readonly_fields = ("id",)
    extra = 1


# Register your models here.
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    form = PatientForm
    list_display = ['identification', 'photo', 'name', 'last_name', 'gender', 'date_born']
    list_display_links = list_display
    fields = ['identification', 'photo', 'photo_tag', 'name', 'last_name', 'date_born', 'address', 'gender',
              'country',
              'who_created', 'creation_date', 'update_date']
    readonly_fields = ('creation_date', 'update_date', 'photo_tag')
    inlines = [PatientComorbidityInline]

    @staticmethod
    def photo_tag(patient):
        if patient.photo:
            return mark_safe('<img src="%s" width="300"/>' % patient.photo.url)
        else:
            return mark_safe('-')


@admin.register(MedicalData)
class MedicalDataAdmin(admin.ModelAdmin):
    list_display = ['patient', 'diagnosis', 'doctor_in_charge', 'status']
    list_display_links = ['patient', 'diagnosis', 'doctor_in_charge']


@admin.register(MedicalHistory)
class MedicalHistoryAdmin(admin.ModelAdmin):
    list_display = ['stay_type', 'patient', 'admission_date', 'date_departure', 'condition']
    list_display_links = list_display


@admin.register(Comorbidity)
class ComorbidityAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = list_display
