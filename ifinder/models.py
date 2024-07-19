from PIL import Image
from django import forms
from django.core.files.uploadedfile import SimpleUploadedFile
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User


class Item(models.Model):
    STATUS_CHOICES = [
        ('perdido', 'Perdido'),
        ('encontrado', 'Encontrado'),
    ]
    Título = models.CharField(max_length=65)
    Descrição = models.TextField(max_length=165)
    Publicada = models.BooleanField(default=False)
    Data = models.DateTimeField(auto_now_add=True)
    Imagem = models.ImageField(null=True, blank=True, max_length=300)
    Autor = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )
    Status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return self.Título
