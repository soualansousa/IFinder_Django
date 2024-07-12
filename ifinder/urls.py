from django.urls import path
from . import views
app_name = 'ifinder'

urlpatterns = [
    path('', views.home, name='home'),
    path('lista-itens/', views.lista_itens, name="itens"),
    path('perdi-item/', views.perdi_item, name='perdi_item'),
    path('encontrei-item/', views.encontrei_item, name='encontrei_item'),
    path('login/', views.login_page),
]
