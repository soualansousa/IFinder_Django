from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from ifinder.models import Item
from ifinder.forms import AdminItemForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse
from django.template.loader import render_to_string
import logging


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
        lista_itens = Item.objects.filter(Devolvido=True)
    elif status == 'publicado':
        lista_itens = Item.objects.filter(Publicado=True)  # Aqui, 'Publicado' deve ser verdadeiro
    elif status == 'pendente':
        lista_itens = Item.objects.filter(Publicado=False)  # Itens não publicados
    else:
        lista_itens = Item.objects.all()
    
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
                return render(request, 'administrativo/pages/cadastro_concluido.html')
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'errors': lista_itens.errors}, status=400)
            else:
                return render(request, "administrativo/pages/encontrei_itemadmin.html", {'itens': lista_itens, 'errors': lista_itens.errors})
    else:
        lista_itens = AdminItemForm()
    return render(request, "administrativo/pages/encontrei_itemadmin.html", {'itens': lista_itens})


def update_item(request, item_id):
    if request.method == "POST":
        try:
            item = get_object_or_404(Item, id=item_id)
            item.Publicado = 'Publicado' in request.POST
            item.Devolvido = 'Devolvido' in request.POST
            item.save()

            # Use 'Items' para corresponder ao que você usa no partial
            updated_item_html = render_to_string('administrativo/partials/item.html', {'Items': item})

            return JsonResponse({'success': True, 'html': updated_item_html})
        except Item.DoesNotExist:
            return JsonResponse({'success': False, 'errors': 'Item não encontrado.'}, status=404)
        except Exception as e:
            return JsonResponse({'success': False, 'errors': str(e)}, status=500)

    return JsonResponse({'success': False, 'errors': 'Método não permitido.'}, status=405)
    
    return JsonResponse({'success': False, 'errors': 'Método não permitido.'}, status=405)
def perdi_itemadmin(request):
    if request.method == "POST":
        lista_itens = AdminItemForm(request.POST, request.FILES, is_admin=True)
        if lista_itens.is_valid():
            item = lista_itens.save(commit=False)
            item.Status = 'perdido'
            item.Autor = request.user
            item.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': True})
            else:
                return render(request, 'administrativo/pages/cadastro_concluido.html')
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'errors': lista_itens.errors}, status=400)
            else:
                return render(request, "administrativo/pages/perdi_itemadmin.html", {'itens': lista_itens, 'errors': lista_itens.errors})
    else:
        lista_itens = AdminItemForm()
    return render(request, "administrativo/pages/perdi_itemadmin.html", {'itens': lista_itens})
