from django.urls import path
from . import views
app_name= 'ifinder'

urlpatterns = [
    path('',views.home),
    path('objetos/',views.objetos),
    path('perdi-objeto/',views.perdi_objeto),
    path('encontrei-objeto/',views.encontrei_objeto),
]
