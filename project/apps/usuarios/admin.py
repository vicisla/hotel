from django.contrib import admin
from .models import InfoUsuario

# Register your models here.
@admin.register(InfoUsuario)
class InfoUsuarioAdmin(admin.ModelAdmin):
    list_display = (
        "usuario",
        "avatar",
        "nacimiento",
        "pais",
        "provincia",
        "ciudad",
        "domicilio",
        "codigo_postal",
        "telefono",
        "dni",
        "cuit",
    )
    search_fields = ("usuario__username",)
  