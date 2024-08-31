from django.conf import settings
from django.urls import path
from . import views

app_name = 'administrativo'

urlpatterns = [
    path('', views.home, name='admin_home'),
    path('lista/', views.lista, name='lista'),
    path('encontrei_itemadmin/', views.encontrei_itemadmin, name='admin_publicar_item')
]
