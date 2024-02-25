from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('home')

def contato(request):
    return HttpResponse('contato ifinder')