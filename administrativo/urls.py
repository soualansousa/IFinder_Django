from django.conf import settings
from django.urls import path
from . import views

app_name = 'administrativo'

urlpatterns = [
    path('', views.home, name='admin_home'),
    path('lista/', views.lista, name='lista'),
    path('publicar-item/<int:item_id>/', views.publicar_item, name='publicar-item'),
    
]
