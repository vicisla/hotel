import pytest
from django.contrib.auth.models import User
from usuarios.models import InfoUsuario

@pytest.fixture
def usuario():
    return User.objects.create(username="usuario1")

@pytest.fixture
def info_usuario(usuario):
    return InfoUsuario.objects.create(usuario= usuario, pais= "Argentina", domicilio="Quintana 2023")

@pytest.mark.django_db
def test_modelos(info_usuario, usuario):
    """"Verificar que los objetos se hayan creado correctamente"""
    assert User.objects.count() == 1
    assert InfoUsuario.objects.count() == 1
    assert info_usuario.usuario == usuario
    