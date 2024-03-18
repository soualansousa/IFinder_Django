from django.shortcuts import render
from utils.ifinder.factory import make_recipe
from .models import Objeto

def home(request):
    return render(request, "ifinder/pages/home.html")

def lista_itens(request):
    objetos= Objeto.objects.filter(is_published=True).order_by('-id')
    return render(request, "ifinder/pages/lista-itens.html", context= {'ifinder': objetos,})

def perdi_item(request):
    return render(request, "ifinder/pages/perdi-item.html")

def encontrei_item(request):
    return render(request, "ifinder/pages/encontrei-item.html")