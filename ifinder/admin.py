from django.contrib import admin

from .models import Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ('Foto', 'Título', 'Descrição', 'Data', 'Autor')
    search_fields = ('Título',)
    list_filter = ['Status',]
    readonly_fields = ['Autor', 'Data', ]
    date_hierarchy = 'Data'


admin.site.register(Item, ItemAdmin)
