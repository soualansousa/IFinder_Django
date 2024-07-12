from django import forms
from .models import Item
from django.contrib.auth.forms import AuthenticationForm


class Formulario(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))