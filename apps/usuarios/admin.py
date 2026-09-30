# pyrefly: ignore [missing-import]
from django.contrib import admin
# pyrefly: ignore [missing-import]
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Rol

# Register your models here.

admin.site.register(Rol)

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Información del Taller', {'fields': ('rol',)}),
    )

