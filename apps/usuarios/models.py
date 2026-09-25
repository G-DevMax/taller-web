from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Usuario(AbstractUser):
    class Rol(models.TextChoices):
        ADMIN = 'ADMIN', 'Administrador'
        MECANICO = 'MECANICO', 'Mecánico'
        RECEPCION = 'RECEPCION', 'Recepcionista'

    rol = models.CharField(
        max_length=20,
        choices=Rol.choices,
        default=Rol.RECEPCION
    )

    telefono = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.username} - {self.get_rol_display()}"

    
