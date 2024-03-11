from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone

# Create your models here.
class TipoHabitacion(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = "Tipo de habitacion"
        verbose_name_plural = "Tipos de habitaciones"

    def __str__(self):
        return self.nombre
    
class Habitacion(models.Model):
    tipo = models.ForeignKey(TipoHabitacion, on_delete=models.CASCADE)
    numero = models.PositiveIntegerField(unique=True)
    precio_x_dia = models.DecimalField(max_digits=10, decimal_places=2,)
    disponible = models.BooleanField(default=False)
    imagen = models.ImageField(upload_to="img/hotel", null=True, blank=True)

    class Meta:
        verbose_name = "Habitacion"
        verbose_name_plural = "Habitaciones"

    def __str__(self):
        return f"Habitacion N° {self.numero}"

# Falta mejorar que cuando se cree una Reserva, la Habitacion reservada este no disponible 
# unicamente para el periodo de tiempo entre fecha_entrada y salida_salida.

class Reserva(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    fecha_entrada = models.DateField()
    fecha_salida = models.DateField()
    precio_total  = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    
    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"

    def clean(self):
        if self.pk: # Si la reserva ya existe (se está actualizando)
            reserva = Reserva.objects.get(pk=self.pk)
            if self.habitacion != reserva.habitacion and not self.habitacion.disponible:
                raise ValidationError("La habitación no está disponible")
        else: # Si es una nueva reserva
            if not self.habitacion.disponible:
                raise ValidationError("La habitación no está disponible")
        if self.fecha_entrada < timezone.now().date():
            raise ValidationError("La fecha de entrada no puede ser anterior al dia actual")
        if self.fecha_salida < timezone.now().date():
            raise ValidationError("La fecha de salida no puede ser anterior al dia actual")
        if self.fecha_salida <= self.fecha_entrada:
            raise ValidationError("La fecha de salida debe ser posterior a la fecha de entrada")
        
    def save(self, *args, **kwargs):
        """Guarda la instancia y calcula el precio total de la reserva segun numero de dias
        entre las fechas de entrada y salida.
        Establece a la habitacion de la reserva como no disponibe"""
        dias = (self.fecha_salida - self.fecha_entrada).days
        self.precio_total = self.habitacion.precio_x_dia * dias
        super().save(*args, **kwargs)
        self.habitacion.disponible = False
        self.habitacion.save()
    
    def delete(self, *args, **kwargs):
        """Establece la Habitacion como disponible cuando se elimina la reserva."""
        self.habitacion.disponible = True
        self.habitacion.save()
        super().delete(*args, **kwargs)
    
    def __str__(self):
        return f"{self.cliente} - {self.habitacion}"