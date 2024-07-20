from django.contrib import admin

from .models import Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ('Foto', 'Título', 'Descrição', 'Data', 'Autor')
    search_fields = ('Título',)
    list_filter = ['Status', 'Devolvido']
    readonly_fields = ['Autor', 'Data', ]
    date_hierarchy = 'Data'

    def mark_as_published(self, request, queryset):
        updated_count = queryset.update(Publicada=True)
        self.message_user(request, f"{updated_count} os itens foram marcados como publicados com sucesso.") # noqa

    def mark_as_returned(self, request, queryset):
        updated_count = queryset.update(Devolvido=True, Publicada=False)
        self.message_user(request, f"{updated_count} os itens foram marcados com sucesso como devolvidos.") # noqa

    mark_as_returned.short_description = "Marcar itens selecionados como devolvidos" # noqa

    mark_as_published.short_description = "Marcar itens selecionados como publicados" # noqa
    actions = [mark_as_published, mark_as_returned]


admin.site.register(Item, ItemAdmin)
