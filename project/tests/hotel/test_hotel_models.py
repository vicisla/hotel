import pytest
from django.contrib.auth.models import User
from hotel.models import TipoHabitacion, Habitacion, Reserva
from django.utils import timezone
from datetime import datetime, timedelta

@pytest.fixture
def tipo_habitacion():
    return TipoHabitacion.objects.create(nombre="Tipo 1", descripcion="Descripción del tipo 1")

@pytest.fixture
def habitacion(tipo_habitacion):
    return Habitacion.objects.create(tipo=tipo_habitacion, numero=1, precio_x_dia=100.00, disponible=True)

@pytest.fixture
def usuario():
    return User.objects.create(username="testuser")

@pytest.fixture
def reserva(usuario, habitacion):
    fecha_actual = timezone.now().date()
    fecha_entrada = fecha_actual + timedelta(days=1)
    fecha_salida = fecha_actual + timedelta(days=5)
    return Reserva.objects.create(cliente=usuario, habitacion=habitacion, fecha_entrada=fecha_entrada, fecha_salida=fecha_salida)

@pytest.mark.django_db
def test_modelos(tipo_habitacion, habitacion, usuario, reserva):
    # Verificar que los objetos se hayan creado correctamente
    assert TipoHabitacion.objects.count() == 1
    assert Habitacion.objects.count() == 1
    assert User.objects.count() == 1
    assert Reserva.objects.count() == 1

    # Verificar los valores de los campos de los objetos
    assert habitacion.tipo == tipo_habitacion
    assert reserva.cliente == usuario
    assert reserva.habitacion == habitacion
    assert reserva.fecha_entrada.strftime("%d-%m-%Y") == (timezone.now().date() + timedelta(days=1)).strftime("%d-%m-%Y")
    assert reserva.fecha_salida.strftime("%d-%m-%Y") == (timezone.now().date() + timedelta(days=5)).strftime("%d-%m-%Y")
    assert reserva.precio_total == 400.00

    # Verificar que la habitación esté marcada como no disponible
    # y verificar que la habitación vuelva a estar disponible al eliminar la reserva
    assert habitacion.disponible == False
    reserva.delete()
    assert habitacion.disponible == True
