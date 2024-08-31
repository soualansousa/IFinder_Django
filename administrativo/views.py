from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from ifinder.models import Item
from ifinder.forms import AdminItemForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse

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

    form = AdminItemForm()

    return render(request, "administrativo/pages/lista.html", {'itens': pagina, 'status': status, 'form': form}) # noqa


def publicar_item(request):
    item = get_object_or_404(Item)
    item.publicado = True
    item.save()
    return render(request, "administrativo/pages/lista.html")


def encontrei_itemadmin(request):
    if request.method == "POST":
        lista_itens = AdminItemForm(request.POST, request.FILES, is_admin=True)
        if lista_itens.is_valid():
            item = lista_itens.save(commit=False)
            item.Status = 'encontrado'
            item.Autor = request.user
            item.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': True})
            else:
                return render(request, 'ifinder/pages/cadastro_concluido.html')
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'errors': lista_itens.errors}, status=400)
            else:
                return render(request, "administrativo/pages/encontrei_itemadmin.html", {'itens': lista_itens, 'errors': lista_itens.errors})
    else:
        lista_itens = AdminItemForm()
    return render(request, "administrativo/pages/encontrei_itemadmin.html", {'itens': lista_itens})
