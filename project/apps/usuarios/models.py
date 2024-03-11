from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class InfoUsuario(models.Model):
    usuario = models.OneToOneField(User, blank=False, null=True, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="img/avatars/%Y/%m/%d", blank=True, null=True) 
    nacimiento = models.DateField(blank=True, null=True)
    pais = models.CharField(max_length=30, blank=True)
    provincia = models.CharField(max_length=40, blank=True)
    ciudad = models.CharField(max_length=40, blank=True)
    domicilio = models.CharField(max_length=80, blank=True)
    codigo_postal = models.CharField(max_length=50, blank=True)
    telefono  = models.CharField(max_length=30, blank=True)
    dni = models.CharField(max_length=30, blank=True)
    cuit = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.usuario.username
