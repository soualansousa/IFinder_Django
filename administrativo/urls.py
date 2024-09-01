from django.conf import settings
from django.urls import path
from . import views
from .views import update_item

app_name = 'administrativo'

urlpatterns = [
    path('', views.home, name='admin_home'),
    path('item/<int:item_id>/update/', update_item, name='update_item'),
    path('lista/', views.lista, name='lista'),
    path('encontrei_itemadmin/', views.encontrei_itemadmin),
    path('perdi_itemadmin/', views.perdi_itemadmin),
]
