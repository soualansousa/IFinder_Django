from django import forms
from .models import Item


class Formulario(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['Título', 'Descrição', 'Imagem', 'Devolvido', 'Publicado']
        exclude = ('Status', )

    def __init__(self, *args, **kwargs):
        is_admin = kwargs.pop('is_admin', False)
        super().__init__(*args, **kwargs)
        if not is_admin:
            self.fields.pop('Devolvido', None)
            self.fields.pop('Publicado', None)


class ItemForm(Formulario):
    def __init__(self, *args, **kwargs):
        kwargs['is_admin'] = False
        super().__init__(*args, **kwargs)

class AdminItemForm(Formulario):
    def __init__(self, *args, **kwargs):
        kwargs['is_admin'] = True
        super().__init__(*args, **kwargs)