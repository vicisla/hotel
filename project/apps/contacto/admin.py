from django.contrib import admin
from .models import Consulta
from .models import Respuesta
# Register your models here.


class RespuestaInline(admin.TabularInline):
    model=Respuesta
    extra=0


class ConsultaAdmin(admin.ModelAdmin):
    inlines = [RespuestaInline]
    list_display = ['mostrar_estado_consulta','fecha', 'nombre','apellido','email',]
    list_filter= ['estado','fecha']

admin.site.register(Consulta, ConsultaAdmin)