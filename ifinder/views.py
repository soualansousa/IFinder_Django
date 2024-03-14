from django.shortcuts import render
from utils.ifinder.factory import make_recipe

def home(request):
    return render(request, "ifinder/pages/home.html")

def lista_itens(request):
    return render(request, "ifinder/pages/lista-itens.html", context= {'ifinder': [make_recipe() for _ in range (10)]})

def perdi_item(request):
    return render(request, "ifinder/pages/perdi-item.html")

def encontrei_item(request):
    return render(request, "ifinder/pages/encontrei-item.html")