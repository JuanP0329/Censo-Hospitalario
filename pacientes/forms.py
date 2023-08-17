from django import forms

from pacientes.models import Patient


class PatientForm(forms.ModelForm):
    id = forms.IntegerField(widget=forms.TextInput(attrs={'width': '100px'}))

    class Meta:
        model = Patient
        fields = '__all__'
