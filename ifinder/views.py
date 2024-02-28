from django.shortcuts import render

def home(request):
    return render(request, "ifinder/pages/home.html")

def objetos(request):
    return render(request, "ifinder/pages/objetos.html")

def perdi_objeto(request):
    return render(request, "ifinder/pages/perdi-objeto.html")

def encontrei_objeto(request):
    return render(request, "ifinder/pages/encontrei-objeto.html")