from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name = 'ifinder'

urlpatterns = [
    path('', views.home, name='home'),
<<<<<<< HEAD
    path('lista-itens/', views.lista_itens, name="itens"),
    path('perdi-item/', views.perdi_item, name='perdi_item'),
    path('encontrei-item/', views.encontrei_item, name='encontrei_item'),
    path('login/', views.user_login, auth_views.login, name='login'),
=======
    path('lista_itens/', views.lista_itens, name="itens"),
    path('perdi_item/', views.perdi_item, name='perdi_item'),
    path('encontrei_item/', views.encontrei_item, name='encontrei_item'),
    path('login/', views.user_login),
>>>>>>> 6b18c12c525a36f12e5141d702f243dd933bdf12
]
