from django.contrib import admin

from .models import Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ('Título', 'Descrição', 'Data', 'Autor')
    search_fields = ('Título',)
    list_filter = ['Status',]
    readonly_fields = ['Autor', 'Data', ]
    date_hierarchy = 'Data'

    def mark_as_found(self, request, queryset):
        updated_count = queryset.update(Status='encontrado')
        self.message_user(request, f"{updated_count} os itens foram marcados como encontrados com sucesso.") # noqa

    mark_as_found.short_description = "Marcar itens selecionados como encontrados" # noqa

    def mark_as_lost(self, request, queryset):
        updated_count = queryset.update(Status='perdido')
        self.message_user(request, f"{updated_count} os itens foram marcados com sucesso como perdidos.") # noqa

    mark_as_lost.short_description = "Marcar itens selecionados como perdidos"

    actions = [mark_as_found, mark_as_lost]


admin.site.register(Item, ItemAdmin)
