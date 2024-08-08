from django import forms
from .models import Item


class Formulario(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['Título', 'Descrição', 'Imagem',]
        exclude = ('Publicada', 'Status', 'Devolvido')
