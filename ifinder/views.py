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
                        'successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid Login')
    else:
        form = LoginForm()
    return render(request, 'ifinder/pages/login_page.html', {'form': form})