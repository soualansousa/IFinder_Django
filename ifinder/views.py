from django.shortcuts import render
from utils.ifinder.factory import make_recipe
from .models import Objeto

def home(request):
    return render(request, "ifinder/pages/home.html")

<<<<<<< HEAD
def objetos(request):
    objetos= Objeto.objects.all()#.order_by('-id')
    return render(request, "ifinder/pages/objetos.html", context= {'ifinder': objetos})
=======
def lista_itens(request):
    objetos= Objeto.objects.filter(is_published=True).order_by('-id')
    return render(request, "ifinder/pages/lista-itens.html", context= {'ifinder': objetos,})
>>>>>>> 7ba2bb55d257463d94a9425851fdcd07ffc1e4df

def perdi_item(request):
    return render(request, "ifinder/pages/perdi-item.html")

def encontrei_item(request):
    return render(request, "ifinder/pages/encontrei-item.html")