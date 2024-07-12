from django.shortcuts import render, HttpResponseRedirect # noqa
from utils.ifinder.factory import make_recipe  # noqa
from .models import Item
from django.urls import reverse_lazy # noqa
from .forms import Formulario, CustomLoginForm
from django.contrib.auth.views import LoginView


def home(request):
    return render(request, "ifinder/pages/home.html")


def lista_itens(request):
    status = request.GET.get('status')
    if status:
        itens = Item.objects.filter(status=status)
    else:
        itens = Item.objects.all()
    
    return render(request, "ifinder/pages/lista-itens.html", {'itens': itens})


def perdi_item(request):
    if request.method == "POST":
        lista_itens = Formulario(request.POST)
        if lista_itens.is_valid():
            item = lista_itens.save(commit=False)
            item.status = 'perdido'
            item.save()
            return render(request, 'ifinder/pages/cadastro-concluido.html')
    else:
        lista_itens = Formulario()
    return render(request, "ifinder/pages/perdi-item.html", {'itens': lista_itens})


def encontrei_item(request):
    if request.method == "POST":
        lista_itens = Formulario(request.POST)
        if lista_itens.is_valid():
            title = lista_itens.cleaned_data['Título'] # noqa
            description = lista_itens.cleaned_data['Descrição'] # noqa
            itens = lista_itens.save() # noqa
            return render(request, 'ifinder/pages/cadastro-concluido.html')
    else:
        lista_itens = Formulario()
    return render(request, "ifinder/pages/encontrei-item.html", {'itens': lista_itens}) # noqa


def login_page(request):
    return render(request, "ifinder/pages/login-page.html")