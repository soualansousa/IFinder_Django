from django.conf import settings
from django.urls import path
from . import views

app_name = 'administrativo'

urlpatterns = [
    path('', views.home, name='admin_home'),
    path('lista/', views.lista, name='lista'),
    path('lista/', views.publicar_item, name='publicar_item'),
    
]
