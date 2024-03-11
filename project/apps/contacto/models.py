from django.db import models
from django.utils.html import format_html

# Create your models here.

class Consulta(models.Model):
    CONTESTADA = "Contestada"
    NO_COMTESTADA = "No contestada"
    EN_PROCESO = "En proceso"
    ESTADO = (
        (CONTESTADA, 'Contestada'),
        (NO_COMTESTADA, 'No contestada'),
        (EN_PROCESO, 'En proceso'),
    )
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    mensaje = models.TextField(max_length=250)
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=50, choices=ESTADO, default="no contestada")
    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.fecha}"
    
    def mostrar_estado_consulta(self):
        if self.estado == "Contestada":
            return format_html('<span style="color: #008000;">{}</span>', self.estado)
        elif self.estado == "No contestada":
            return format_html('<span style="color: #ff0000;">{}</span>', self.estado)
        elif self.estado == "En proceso":
            return format_html('<span style="color: #ffa500;">{}</span>', self.estado)
        
class Respuesta(models.Model):
    consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE)
    respuesta = models.CharField(max_length=250)
    fecha = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.consulta} - {self.fecha}"

    def create_mensaje(self,):
        consulta_cambio_estado = Consulta.objects.get(id= self.consulta.id)
        consulta_cambio_estado.estado = "Contestada"
        consulta_cambio_estado.save()
        # Logica envio de email



    def save (self, *args, **kwargs):
        self.create_mensaje()   
        force_update = False
        if self.id:
            force_update = True
        super(Respuesta, self).save(force_update=force_update)