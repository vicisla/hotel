from django.urls import path
from . import views

urlpatterns = [
   
    path("infousuario/detail/<int:pk>", views.InfoUsuarioDetail.as_view(), name="infousuario_detail"),
    path("infousuario/create/", views.InfoUsuarioCreate.as_view(), name="infousuario_create"),
    path("infousuario/update/<int:pk>", views.InfoUsuarioUpdate.as_view(), name="infousuario_update"),
    path("infousuario/delete/<int:pk>", views.InfoUsuarioDelete.as_view(), name="infousuario_delete"),
]