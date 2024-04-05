from django import forms
class InsereitemForm(forms.Form):
    nome= forms.CharField(
        label='Nome do item', max_length=65
    )
    descricao= forms.CharField(
        label='descrição do item', max_length=165
    )