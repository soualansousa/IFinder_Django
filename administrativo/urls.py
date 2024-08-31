from django.conf import settings
from django.urls import path
from . import views

app_name = 'administrativo'

urlpatterns = [
    path('', views.home, name='admin_home'),
    path('lista/', views.lista, name='lista'),
    path('encontrei_itemadmin/', views.encontrei_itemadmin),
    path('perdi_itemadmin/', views.perdi_itemadmin),
    path('item/<int:item_id>/update/', views.update_item, name='update_item'),
]
