from django.urls import path
from ifinder.views import home, contato

urlpatterns = [
    path('',home),
    path('contato/',contato),
]
