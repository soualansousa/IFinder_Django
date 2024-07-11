from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User


class Item(models.Model):
    Título = models.CharField(max_length=65)
    Descrição = models.CharField(max_length=165)
    Publicada = models.BooleanField(default=False)
    Data = models.DateTimeField(auto_now_add=True)
    Autor = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.title
