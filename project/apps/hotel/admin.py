from django.contrib import admin
from . import models

# Register your models here.
admin.site.site_title = "Shipibo Hotel"
admin.site.site_header = "Shipibo Hotel Administración"
admin.site.index_title = "Panel de control"

class HabitacionInline(admin.TabularInline):
    model = models.Habitacion
    extra = 0

class ReservaInline(admin.TabularInline):
    model = models.Reserva
    extra = 0


@admin.register(models.TipoHabitacion)
class TipoHabitacionAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion",)
    search_fields = ("nombre",)
    list_filter = ("nombre",)
    ordering = ("nombre",)
    inlines = [HabitacionInline]

@admin.register(models.Habitacion)
class HabitacionAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Relación", {"fields": ["tipo"]}),
        (
            "Datos generales",
            {
                "fields": [
                    'numero', 'precio_x_dia', 'disponible' , 'imagen'
                ]
            },
        ),
    ]
    list_display = (
        "tipo",
        "numero",
        "precio_x_dia",
        "disponible",
        "imagen",
    )
    search_fields = ("tipo__nombre","numero",)
    list_filter = ("tipo__nombre", "disponible",)
    ordering = ("tipo","-numero",)
    list_display_links=("tipo","numero",)
    inlines = [ReservaInline]
    actions = ["habitacion_disponible", "habitacion_no_disponible"]

    def set_disponibilidad(self, request, queryset, value):
        registro = queryset.update(disponible=value)
        if registro == 1:
            mensaje = "Registro actualizado"
        else:
            mensaje = "%s registros actualizados" % registro
        self.message_user(request, "%s exitosamente." % mensaje)

    def habitacion_disponible(self, request, queryset):
        self.set_disponibilidad(request, queryset, True)
    habitacion_disponible.short_description = "Establecer como disponible"

    def habitacion_no_disponible(self, request, queryset):
        self.set_disponibilidad(request, queryset, False)
    habitacion_no_disponible.short_description = "Establecer como no disponible"

@admin.register(models.Reserva)
class ReservaAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Relación", {"fields": ["cliente", "habitacion"]}),
        (
            "Datos generales",
            {
                "fields": [
                    'Fecha_entrada', 'Fecha_salida'
                    ]
            },
        ),
    ]
    list_display = (
        "cliente",
        "habitacion",
        "fecha_entrada",
        "fecha_salida",
        "precio_total",
    )
    search_fields = ("cliente__username", "habitacion__tipo__nombre",)
    list_filter = ("fecha_entrada", "fecha_salida")
    list_display_links=("cliente","habitacion",)
    ordering = ("-fecha_entrada",)


