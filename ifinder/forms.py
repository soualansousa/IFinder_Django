from django import forms
from .models import Objeto


class Formulario(forms.ModelForm):
    class Meta:
        model = Objeto
        fields = '__all__'
