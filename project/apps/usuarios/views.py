from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import DetailView
from django.urls import reverse_lazy
from .forms import InfoUsuarioForm
from .models import InfoUsuario
from django.contrib import messages

# Create your views here.
class InfoUsuarioDetail(LoginRequiredMixin, DetailView):
    model = InfoUsuario
    
class InfoUsuarioCreate(LoginRequiredMixin, CreateView):
    model = InfoUsuario
    form_class = InfoUsuarioForm
    success_url = reverse_lazy('home:index')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        messages.success(self.request, "Se guardo la informacion de perfil correctamente.", extra_tags="alert alert-success")
        return super().form_valid(form)
   
    
class InfoUsuarioUpdate(LoginRequiredMixin, UpdateView):
    model= InfoUsuario
    form_class = InfoUsuarioForm
    success_url = reverse_lazy('home:index')
    def form_valid(self, form):
        messages.success(self.request, "Se actualizo la informacion de perfil correctamente.", extra_tags="alert alert-success")
        return super().form_valid(form)

    
class InfoUsuarioDelete(LoginRequiredMixin, DeleteView):
    model= InfoUsuario
    success_url = reverse_lazy("home:index")
    def get_success_url(self):
        messages.success(self.request, "Informacion de perfil eliminada correctamente.", extra_tags="alert alert-danger")
        return super().get_success_url()
