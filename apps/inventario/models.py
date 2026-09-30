# pyrefly: ignore [missing-import]
from django.db import models

# Create your models here.

class Items(models.Model):
    class TipoProducto(models.Choices):
        REPUESTO_AUTO = 'Repuesto de Auto'
        REPUESTO_MOTO = 'Repuesto de Moto'
        ACCESORIO = 'Accesorio'
        HERRAMIENTA = 'Herramienta'
        OTRO = 'Otro'
    
    tipo_producto = models.CharField(
        max_length=30,
        choices=TipoProducto.choices,
        default=TipoProducto.REPUESTO_AUTO
    )

    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=12, decimal_places=0, default=0, help_text="Precio Unitario (PYG)")
    stock = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Item de Inventario"
        verbose_name_plural = "Items de Inventario"
        db_table = "items"

    def __str__(self):
        return f"{self.descripcion} - PYG:{self.precio} - Stock: {self.stock}"