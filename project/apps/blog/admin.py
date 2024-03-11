from django.contrib import admin
from .models import Reseña

# Register your models here.
@admin.register(Reseña)
class ReseñaAdmin(admin.ModelAdmin):
    list_display = (
        "titulo",
        "contenido",
        "autor",
        "color_calificacion",
        "imagen",
        "fecha",
    )
    search_fields = ("autor__username", "titulo")
    ordering = ("fecha",)
    list_display_links = ("titulo", "contenido",)
    list_filter = ("fecha","autor","calificacion")
    