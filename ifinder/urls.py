from django.urls import path
from . import views
app_name= 'ifinder'

urlpatterns = [
    path('',views.home ),
    path('lista-itens/',views.lista_itens),
    path('perdi-item/',views.perdi_item),
    path('encontrei-item/',views.encontrei_item),
]
