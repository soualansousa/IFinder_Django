from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe


class Item(models.Model):
    STATUS_CHOICES = [
        ('perdido', 'Perdido'),
        ('encontrado', 'Encontrado'),
    ]
    Título = models.CharField(max_length=65)
    Descrição = models.TextField(max_length=165)
    Publicada = models.BooleanField(default=False)
    Data = models.DateTimeField(auto_now_add=True)
    Imagem = models.ImageField(null=True, max_length=300)
    Autor = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
        )
    Devolvido = models.BooleanField(default=False)
    Status = models.CharField(max_length=10, choices=STATUS_CHOICES) # noqa

    def __str__(self):
        return self.Título

    def Foto(self):
        self.Imagem
        return mark_safe('<img src="{}" height="50" />' .format(self.Imagem.url)) # noqa
