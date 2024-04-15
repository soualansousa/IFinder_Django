from django.shortcuts import render
from utils.ifinder.factory import make_recipe  # noqa
from .models import Item


def home(request):
    return render(request, "ifinder/pages/home.html")


def lista_itens(request):
    itens = Item.objects.all()  # .order_by('-id')

    return render(request, "ifinder/pages/lista-itens.html", context={'itens': itens})  # noqa


def perdi_item(request):
    return render(request, "ifinder/pages/perdi-item.html")


def encontrei_item(request):
    return render(request, "ifinder/pages/encontrei-item.html")
