from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .admin import admin_site

app_name = 'ifinder'

urlpatterns = [
    path('admin/', admin_site.urls),
    path('admin/custom-dashboard/', views.custom_dashboard, name='custom_dashboard'),
    path('', views.user_login, name='login'),
    path('home/', views.home, name='home'),
    path('home/lista_itens/', views.lista_itens, name="lista_itens"),
    path('home/perdi_item/', views.perdi_item, name='perdi_item'),
    path('home/encontrei_item/', views.encontrei_item, name='encontrei_item'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # noqa