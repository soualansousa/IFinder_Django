from django.shortcuts import render, HttpResponseRedirect # noqa
from utils.ifinder.factory import make_recipe  # noqa
from .models import Item
from django.urls import reverse_lazy # noqa
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
            title = lista_itens.cleaned_data['title'] # noqa
            description = lista_itens.cleaned_data['description']# noqa
            itens = lista_itens.save() # noqa
            return render(request, 'ifinder/pages/cadastro-concluido.html')
    else:
        lista_itens = Formulario()
    return render(request, "ifinder/pages/perdi-item.html", {'itens': lista_itens}) # noqa


# def encontrei_item(request):
#     return render(request, "ifinder/pages/encontrei-item.html")

def encontrei_item(request):
    if request.method == "POST":
        lista_itens = Formulario(request.POST)
        if lista_itens.is_valid():
            title = lista_itens.cleaned_data['title'] # noqa
            description = lista_itens.cleaned_data['description'] # noqa
            itens = lista_itens.save() # noqa
            return render(request, 'ifinder/pages/cadastro-concluido.html')
    else:
        lista_itens = Formulario()
    return render(request, "ifinder/pages/encontrei-item.html", {'itens': lista_itens}) # noqa