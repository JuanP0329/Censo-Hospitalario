from django import forms

from doctores.models import Doctor


class DoctorForm(forms.ModelForm):
    identification = forms.IntegerField(widget=forms.TextInput(attrs={'width': '100px'}))

    class Meta:
        model = Doctor
        fields = '__all__'
