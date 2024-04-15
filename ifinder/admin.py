from django.contrib import admin

from .models import Item


class ItemAdmin(admin.ModelAdmin):
    ...


admin.site.register(Item, ItemAdmin)
