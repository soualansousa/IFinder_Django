from django.shortcuts import render
from utils.ifinder.factory import make_recipe

def home(request):
    return render(request, "ifinder/pages/home.html")

def objetos(request):
    return render(request, "ifinder/pages/objetos.html", context= {'ifinder': [make_recipe() for _ in range (10)]})

def perdi_objeto(request):
    return render(request, "ifinder/pages/perdi-objeto.html")

def encontrei_objeto(request):
    return render(request, "ifinder/pages/encontrei-objeto.html")