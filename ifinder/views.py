from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('home')

def index(request):
    return render(request, "ifinder/pages/index.html")

def contato(request):
    return HttpResponse('contato ifinder')