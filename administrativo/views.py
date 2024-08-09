from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from ifinder.models import Item

# Create your views here.


@login_required
def home(request):
    return render(request, "administrativo/pages/home.html")


def lista(request):
    itens = Item.objects.all()
    return render(request, "administrativo/pages/lista.html", {'itens': itens})


def publicar_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.publicado = True
    item.save()
    return redirect('lista-itens-admin')
