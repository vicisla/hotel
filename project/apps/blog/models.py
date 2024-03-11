from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html

# Create your models here.
class Reseña(models.Model):
    OPCIONES_CALIFICACION = [
        (1, '1 - Malo'),
        (2, '2 - Regular'),
        (3, '3 - Promedio'),
        (4, '4 - Bueno'),
        (5, '5 - Excelente'),
    ]
    titulo = models.CharField(max_length=50)
    contenido = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    calificacion = models.IntegerField(choices=OPCIONES_CALIFICACION)
    imagen = models.ImageField(upload_to='img/blog', null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    
    def color_calificacion(self):
        if self.calificacion < 3:
            return format_html('<span style="color: #ff0000;">{}</span>', self.calificacion)
        elif self.calificacion == 3:
            return format_html('<span style="color: #ffa500;">{}</span>', self.calificacion)
        elif self.calificacion >3:
            return format_html('<span style="color: #008000;">{}</span>', self.calificacion)
  