from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path("", TemplateView.as_view(template_name="blog/index.html"), name="index"),
    path("reseña/detail/<int:pk>", views.ReseñaDetail.as_view(), name="reseña_detail"),
    path("reseña/list/", views.ReseñaList.as_view(), name="reseña_list"),
    path("reseña/create/", views.ReseñaCreateView.as_view(), name="reseña_create"),
    path("reseña/delete/<int:pk>", views.ReseñaDelete.as_view(), name="reseña_delete"),
    path("reseña/update/<int:pk>", views.ReseñaUpdate.as_view(), name="reseña_update"),
]