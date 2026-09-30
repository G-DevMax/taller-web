# pyrefly: ignore [missing-import]
from django.db import models
# pyrefly: ignore [missing-import]
from django.conf import settings
# pyrefly: ignore [missing-import]
from django.utils import timezone

# Create your models here.

class Marca(models.Model):
    marca = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"
        db_table = "Marcas"

    def __str__(self):
        return self.marca

class Vehiculos(models.Model):
    # clases relacionadas al vehiculo y datos predeterminados
    class EstadoVehiculo(models.Choices):
        RECIBIDO = "Recibido"
        EN_ESPERA = "En Espera"
        EN_DIAGNOSTICO = "En Diagnóstico"
        PENDIENTE_APROBACION = "Pendiente de Aprobación"
        ESPERANDO_REPUESTOS = "Esperando Repuestos"
        EN_REPARACION = "En Reparación"
        LISTO_PARA_RETIRO = "Listo para Retiro"
        ENTREGADO = "Entregado"
        CANCELADO = "Cancelado"
    
    class Tipo(models.Choices):
        AUTO = "Auto"
        MOTO = "Moto"
        CAMIONETA = "Camioneta"
    
    class MotivoIngreso(models.Choices):
        REVISION_GENERAL = "Revisión General"
        MANTENIMIENTO = "Mantenimiento"
        REPARACION = "Reparación"
        INSTALACION = "Instalación"
        OTRO = "Otro"

    #campos de la tabla vehiculos
    descripcion = models.TextField()

    tipo = models.CharField(
        max_length=10,
        choices=Tipo.choices,
        default=Tipo.AUTO
    )

    chapa = models.TextField()

    marca = models.ForeignKey(
        Marca,
        on_delete=models.PROTECT,
        related_name="vehiculos"
    )
    
    motivo_ingreso = models.CharField(
        max_length=60,
        choices=MotivoIngreso.choices,
        default=MotivoIngreso.REVISION_GENERAL
    )

    fecha_ingreso = models.DateTimeField(
        default=timezone.now
    )

    fecha_salida = models.DateTimeField(
        null=True,
        blank=True
    )

    estado = models.CharField(
        max_length=60,
        choices=EstadoVehiculo.choices,
        default=EstadoVehiculo.RECIBIDO
    )

    class Meta:
        verbose_name = "Vehiculo"
        verbose_name_plural = "Vehiculos"
        db_table = "Vehiculos"

    def __str__(self):
        return f"{self.descripcion} - {self.chapa}"

# tabla de historial de cambios (cambios generales de toda la DB)
    class HistorialCambios(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='historial_cambios'
    )
    # campos con los datos cambiados, añadidos o eliminados
    entidad = models.CharField(max_length=50, help_text="Tabla o modelo afectado (ej. Vehiculo, Item)")
    id_entidad = models.PositiveIntegerField(help_text="ID del registro modificado")
    accion = models.CharField(max_length=50, help_text="CREAR, MODIFICAR, ELIMINAR, etc.")
    # se guarda en un JSON los campos modificados, añadidos o eliminados
    detalle = models.JSONField(null=True, blank=True, help_text="Snapshot o campos modificados")
    fecha_cambio = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Historial de Cambio'
        verbose_name_plural = 'Historial de Cambios'
        db_table = 'historial_cambios'

    def __str__(self):
        return f"{self.accion} en {self.entidad} #{self.id_entidad} ({self.fecha_cambio.strftime('%d/%m/%Y %H:%M')})"




    