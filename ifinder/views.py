from django.shortcuts import render, HttpResponseRedirect # noqa
from utils.ifinder.factory import make_recipe  # noqa
from .models import Item
from django.urls import reverse_lazy # noqa
from .forms import Formulario,LoginForm
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login


def home(request):
    return render(request, "ifinder/pages/home.html")


def lista_itens(request):
    itens = Item.objects.all()  # .order_by('-id')

    return render(request, "ifinder/pages/lista-itens.html", context={'itens': itens})  # noqa


def perdi_item(request):
    if request.method == "POST":
        lista_itens = Formulario(request.POST)
        if lista_itens.is_valid():
            title = lista_itens.cleaned_data['Título'] # noqa
            description = lista_itens.cleaned_data['Descrição']# noqa
            itens = lista_itens.save() # noqa
            return render(request, 'ifinder/pages/cadastro-concluido.html')
    else:
        lista_itens = Formulario()
    return render(request, "ifinder/pages/perdi-item.html", {'itens': lista_itens}) # noqa


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


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],
                   password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated',
                        successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid Login')
    else:
        form = LoginForm()
    return render(request, 'sua-app/login.html', {'form': form})