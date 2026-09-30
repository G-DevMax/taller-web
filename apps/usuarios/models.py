# pyrefly: ignore [missing-import]
from django.contrib.auth.models import AbstractUser
# pyrefly: ignore [missing-import]
from django.db import models

# Create your models here.
# Tabla de Roles
class Rol(models.Model):
    rol = models.CharField(max_length=30, unique=True)

    class Meta:
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'
        db_table = 'roles'

    def __str__(self):
        return self.nombre

# Tabla de Usuarios (predeterminado de Django)
class Usuario(AbstractUser):
    # Se le añade una foreign key a la tabla de Roles
    rol = models.ForeignKey(
        Rol, 
        on_delete=models.PROTECT, 
        null=False, 
        blank=False,
        related_name='usuarios'
    )

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        db_table = 'usuarios'

    def __str__(self):
        return f"{self.username} - {self.get_rol_display()}"

    
