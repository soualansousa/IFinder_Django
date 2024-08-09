from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ifinder.models import Item

# Create your views here.


@login_required
def home(request):
    return render(request, "administrativo/pages/home.html")


def lista(request):
    itens = Item.objects.all()
    return render(request, "administrativo/pages/lista.html", {'itens': itens})
