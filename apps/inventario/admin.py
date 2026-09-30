# pyrefly: ignore [missing-import]
from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('descripcion', 'tipo_producto', 'precio', 'stock')
    list_filter = ('tipo_producto',)
    search_fields = ('descripcion',)