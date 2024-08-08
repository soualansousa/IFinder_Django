from django.shortcuts import render, redirect
from .models import Item
from .forms import Formulario
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


@login_required
def home(request):
    return render(request, "ifinder/pages/home.html")


def lista_itens(request):
    status = request.GET.get('status', 'todos')

    if status == 'perdido':
        lista_itens = Item.objects.filter(Status='perdido', Publicada=True)
    elif status == 'encontrado':
        lista_itens = Item.objects.filter(Status='encontrado', Publicada=True)
    else:
        lista_itens = Item.objects.filter(Publicada=True)

    lista_paginada = Paginator(lista_itens, 5)
    p = request.GET.get("p")
    try:
        pagina = lista_paginada.page(p)
    except PageNotAnInteger:
        pagina = lista_paginada.page(1)
    except EmptyPage:
        pagina = lista_paginada.page(1)

    return render(request, "ifinder/pages/lista_itens.html", {'itens': pagina, 'status': status}) # noqa


def perdi_item(request):
    if request.method == "POST":
        lista_itens = Formulario(request.POST, request.FILES)
        if lista_itens.is_valid():
            item = lista_itens.save(commit=False)
            item.Status = 'perdido'
            item.Autor = request.user
            item.save()
            return render(request, 'ifinder/pages/cadastro_concluido.html')
    else:
        lista_itens = Formulario()

    return render(request, "ifinder/pages/perdi_item.html", {'itens': lista_itens}) # noqa


def encontrei_item(request):
    if request.method == "POST":
        lista_itens = Formulario(request.POST, request.FILES)
        if lista_itens.is_valid():
            item = lista_itens.save(commit=False)
            item.Status = 'encontrado'
            item.Autor = request.user
            item.save()
            return render(request, 'ifinder/pages/cadastro_concluido.html')
        else:
            print(lista_itens.errors)
    else:
        lista_itens = Formulario()
    return render(request, "ifinder/pages/encontrei_item.html", {'itens': lista_itens}) # noqa


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
        
            if form.get_user().is_superuser:
                return redirect("administrativo:home")
            
            return redirect("ifinder:home")
    else:
        form = AuthenticationForm()
    return render(request, 'ifinder/pages/login_page.html', {'form': form})
