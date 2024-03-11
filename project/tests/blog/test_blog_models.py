import pytest
from django.contrib.auth.models import User
from blog.models import Reseña

@pytest.fixture
def usuario():
    return User.objects.create(username="usuario1")

@pytest.fixture
def reseña(usuario):
    return Reseña.objects.create(titulo='Mi Reseña', contenido='Esta es mi reseña', autor=usuario, calificacion=4)

@pytest.mark.django_db
def test_modelos(reseña, usuario):
    # Verificar que los objetos se hayan creado correctamente
    assert User.objects.count() == 1
    assert Reseña.objects.count() == 1
    assert reseña.autor == usuario