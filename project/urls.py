from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from ifinder import views
from ifinder.admin import admin_site


urlpatterns = [
    path('admin/custom-dashboard/', views.custom_dashboard,),
    path('admin/', admin.site.urls),
    path('',include('ifinder.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)