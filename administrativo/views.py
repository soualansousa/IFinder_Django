from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from ifinder.models import Item
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.


@login_required
def home(request):
    return render(request, "administrativo/pages/home.html")


def lista(request):
    status = request.GET.get('status', 'todos')

    if status == 'perdido':
        lista_itens = Item.objects.filter(Status='perdido')
    elif status == 'encontrado':
        lista_itens = Item.objects.filter(Status='encontrado')
    elif status == 'devolvido':
        lista_itens = Item.objects.filter(Status='encontrado')
    elif status == 'publicado':
        lista_itens = Item.objects.filter(Status='encontrado')
    else:
        lista_itens = Item.objects.filter()

    lista_paginada = Paginator(lista_itens, 5)
    p = request.GET.get("p")
    try:
        pagina = lista_paginada.page(p)
    except PageNotAnInteger:
        pagina = lista_paginada.page(1)
    except EmptyPage:
        pagina = lista_paginada.page(1)

    return render(request, "administrativo/pages/lista.html", {'itens': pagina, 'status': status}) # noqa


def publicar_item(request):
    item = get_object_or_404(Item)
    item.publicado = True
    item.save()
    return render(request, "administrativo/pages/lista.html")

