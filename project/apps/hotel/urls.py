from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    # Tipo de habitacion
    path("tipohabitacion/detail/<int:pk>", views.TipoHabitacionDetail.as_view(), name="tipohabitacion_detail"),
    path("tipohabitacion/list/", views.TipoHabitacionList.as_view(), name="tipohabitacion_list"),
    path("tipohabitacion/create/", views.TipoHabitacionCreateView.as_view(), name="tipohabitacion_create"),
    path("tipohabitacion/delete/<int:pk>", views.TipoHabitacionDelete.as_view(), name="tipohabitacion_delete"),
    path("tipohabitacion/update/<int:pk>", views.TipoHabitacionUpdate.as_view(), name="tipohabitacion_update"),
    # Habitacion
    path("habitacion/detail/<int:pk>", views.HabitacionDetail.as_view(), name="habitacion_detail"),
    path("habitacion/list/", views.HabitacionList.as_view(), name="habitacion_list"),
    path("habitacion/create/", views.HabitacionCreateView.as_view(), name="habitacion_create"),
    path("habitacion/delete/<int:pk>", views.HabitacionDelete.as_view(), name="habitacion_delete"),
    path("habitacion/update/<int:pk>", views.HabitacionUpdate.as_view(), name="habitacion_update"),
    # Reserva
    path("reserva/detail/<int:pk>", views.ReservaDetail.as_view(), name="reserva_detail"),
    path("reserva/list/", views.ReservaList.as_view(), name="reserva_list"),
    path("reserva/create/", views.ReservaCreateView.as_view(), name="reserva_create"),
    path("reserva/delete/<int:pk>", views.ReservaDelete.as_view(), name="reserva_delete"),
    path("reserva/update/<int:pk>", views.ReservaUpdate.as_view(), name="reserva_update"),
]

