from django.shortcuts import render, HttpResponseRedirect, redirect # noqa
from utils.ifinder.factory import make_recipe  # noqa
from .models import Item
from django.urls import reverse_lazy # noqa
from .forms import Formulario,LoginForm
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

def home(request):
    return render(request, "ifinder/pages/home.html")


def lista_itens(request):
    status = request.GET.get('status', 'todos')
    if status == 'perdido':
        itens = Item.objects.filter(Status='perdido', Publicada=True)
    elif status == 'encontrado':
        itens = Item.objects.filter(Status='encontrado', Publicada=True)
    else:
        itens = Item.objects.filter(Publicada=True)
    
    return render(request, "ifinder/pages/lista_itens.html", {'itens': itens, 'status': status})


def perdi_item(request):
    if request.method == "POST":
        lista_itens = Formulario(request.POST)
        if lista_itens.is_valid():
            item = lista_itens.save(commit=False)
            item.Status = 'perdido'
            item.save()
            return render(request, 'ifinder/pages/cadastro_concluido.html')
    else:
        lista_itens = Formulario()
    return render(request, "ifinder/pages/perdi_item.html", {'itens': lista_itens}) # noqa


def encontrei_item(request):
    if request.method == "POST":
        lista_itens = Formulario(request.POST)
        if lista_itens.is_valid():
            item = lista_itens.save(commit=False)
            item.Status = 'encontrado'
            item.save()
            return render(request, 'ifinder/pages/cadastro_concluido.html')
    else:
        lista_itens = Formulario()
    return render(request, "ifinder/pages/encontrei_item.html", {'itens': lista_itens}) # noqa


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("ifinder:login_page")
    else:
        form = AuthenticationForm()
    return render(request, 'ifinder/pages/login_page.html', {'form': form})