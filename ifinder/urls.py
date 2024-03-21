from django.urls import path
from . import views
app_name= 'ifinder'

urlpatterns = [
    path('',views.home, name= "home"),
    path('objetos/',views.objetos, name="objetos"),
    path('perdi-objeto/',views.perdi_objeto),
    path('encontrei-objeto/',views.encontrei_objeto),
]
