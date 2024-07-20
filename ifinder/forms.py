from django import forms
from .models import Item
from django.contrib.auth.forms import AuthenticationForm # noqa


class Formulario(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
        exclude = ('Publicada', 'Status')
