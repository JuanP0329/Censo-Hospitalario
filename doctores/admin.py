from django.contrib import admin
from django.utils.safestring import mark_safe

from .forms import DoctorForm
from .models import Doctor, Specialty


# Register your models here.

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    form = DoctorForm
    list_display = ['identification', 'photo', 'name', 'last_name', 'email', 'specialty']
    list_display_links = list_display
    fields = ['identification', 'photo', 'photo_tag', 'name', 'last_name', 'email', 'specialty']
    readonly_fields = ['photo_tag']
    search_fields = ['identification', 'name', 'last_name']

    @staticmethod
    def photo_tag(doctor):
        if doctor.photo:
            return mark_safe('<img src="%s" width="300"/>' % doctor.photo.url)
        else:
            return mark_safe('-')


@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = list_display
