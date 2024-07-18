from django.urls import path
from . import views
app_name = 'ifinder'

urlpatterns = [
    path('', views.user_login, name='login'),
    path('home/', views.home, name='home'),
    path('lista_itens/', views.lista_itens, name="lista_itens"),
    path('perdi_item/', views.perdi_item, name='perdi_item'),
    path('encontrei_item/', views.encontrei_item, name='encontrei_item'),
]
