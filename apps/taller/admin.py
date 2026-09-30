# pyrefly: ignore [missing-import]
from django.contrib import admin
from .models import Marca, Vehiculo, HistorialCambio

admin.site.register(Marca)

@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('chapa', 'marca', 'descripcion', 'estado', 'fecha_ingreso', 'fecha_salida')
    list_filter = ('estado', 'marca')
    search_fields = ('chapa', 'descripcion', 'motivo_ingreso')

@admin.register(HistorialCambio)
class HistorialCambioAdmin(admin.ModelAdmin):
    list_display = ('fecha_cambio', 'usuario', 'accion', 'entidad', 'id_entidad')
    list_filter = ('accion', 'entidad')