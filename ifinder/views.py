from django.shortcuts import render, HttpResponseRedirect
from utils.ifinder.factory import make_recipe  # noqa
from .models import Item
from django.urls import reverse_lazy
from .forms import Formulario


def home(request):
    return render(request, "ifinder/pages/home.html")


def lista_itens(request):
    itens = Item.objects.all()  # .order_by('-id')

    return render(request, "ifinder/pages/lista-itens.html", context={'itens': itens})  # noqa


def perdi_item(request):
    if request.method == "POST":
        lista_itens = Formulario(request.POST)
        if lista_itens.is_valid():
            title = lista_itens.cleaned_data['title']
            description = lista_itens.cleaned_data['description']
            itens = lista_itens.save()
            return render(request, 'ifinder/pages/cadastro-concluido.html')
    else:
        lista_itens = Formulario()
    return render(request, "ifinder/pages/perdi-item.html", {'itens': lista_itens})


# def encontrei_item(request):
#     return render(request, "ifinder/pages/encontrei-item.html")

def encontrei_item(request):
    if request.method == "POST":
        lista_itens = Formulario(request.POST)
        if lista_itens.is_valid():
            title = lista_itens.cleaned_data['title']
            description = lista_itens.cleaned_data['description']
            itens = lista_itens.save()
            return render(request, 'ifinder/pages/cadastro-concluido.html')
    else:
        lista_itens = Formulario()
    return render(request, "ifinder/pages/encontrei-item.html", {'itens': lista_itens})