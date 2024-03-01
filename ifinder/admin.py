from django.contrib import admin

from .models import Objeto

class ObjetoAdmin(admin.ModelAdmin):
    ...

admin.site.register(Objeto, ObjetoAdmin)