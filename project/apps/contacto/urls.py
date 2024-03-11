from django.urls import path
from .views import ConsultaFormView


urlpatterns = [
    path("", ConsultaFormView.as_view(template_name="contacto/index.html"), name="index"),
]