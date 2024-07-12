from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name = 'ifinder'

urlpatterns = [
    path('', views.home, name='home'),
    path('lista_itens/', views.lista_itens, name="itens"),
    path('perdi_item/', views.perdi_item, name='perdi_item'),
    path('encontrei_item/', views.encontrei_item, name='encontrei_item'),
    path('login/', views.user_login, auth_views.login, name='login'),
]
