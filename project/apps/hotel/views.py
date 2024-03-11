from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from . import models, forms 
from django.contrib import messages


#   Index hotel
class IndexView(TemplateView):
    template_name = "hotel/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["habitaciones"] = models.Habitacion.objects.all()
        return context
    
# Tipo de Habitacion

class TipoHabitacionDetail(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = models.TipoHabitacion
    def test_func(self):
        """ Devuelve True si el usuario es del staff."""
        return self.request.user.is_staff
    

class TipoHabitacionList(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = models.TipoHabitacion
    def get_queryset(self):
        """Filtra todos los tipos de habitaciones que contengan el texto ingresado."""
        if self.request.GET.get("consulta"):
            query = self.request.GET.get("consulta")
            object_list = models.TipoHabitacion.objects.filter(nombre__icontains=query)
        else:
            object_list = models.TipoHabitacion.objects.all()
        return object_list
    def test_func(self):
        """ Devuelve True si el usuario es del staff."""
        return self.request.user.is_staff

class TipoHabitacionCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = models.TipoHabitacion
    form_class = forms.TipoHabitacionForm
    success_url = reverse_lazy("hotel:tipohabitacion_list")

    def form_valid(self, form):
        messages.success(self.request, "Tipo de habitacion creada correctamente.", extra_tags="alert alert-success")
        return super().form_valid(form)
    def test_func(self):
        """ Devuelve True si el usuario tiene permiso."""
        return self.request.user.has_perm('hotel.add_tipohabitacion')

class TipoHabitacionDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.TipoHabitacion
    template_name = "hotel/confirm_delete.html"
    success_url = reverse_lazy("hotel:tipohabitacion_list")

    def get_success_url(self):
            messages.success(self.request, "Tipo de habitacion eliminada correctamente.", extra_tags="alert alert-danger")
            return super().get_success_url()
    
    def test_func(self):
        """ Devuelve True si el usuario tiene permiso."""
        return self.request.user.has_perm('hotel.delete_tipohabitacion')

class TipoHabitacionUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.TipoHabitacion
    success_url = reverse_lazy("hotel:tipohabitacion_list")
    form_class = forms.TipoHabitacionForm

    def form_valid(self, form):
        messages.success(self.request, "Tipo de habitacion actualizada correctamente.", extra_tags="alert alert-success")
        return super().form_valid(form)
    def test_func(self):
        """ Devuelve True si el usuario tiene permiso."""
        return self.request.user.has_perm('hotel.change_tipohabitacion')

# Habitacion

class HabitacionDetail(LoginRequiredMixin, DetailView):
    model = models.Habitacion

class HabitacionList(LoginRequiredMixin, ListView):
    model = models.Habitacion
    def get_queryset(self):
        """Filtra todas las habitaciones que contengan el texto ingresado."""
        if self.request.GET.get("consulta"):
            query = self.request.GET.get("consulta")
            object_list = models.Habitacion.objects.filter(numero__icontains=query)
        else:
            object_list = models.Habitacion.objects.all()
        return object_list

class HabitacionCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = models.Habitacion
    form_class = forms.HabitacionForm
    success_url = reverse_lazy("hotel:habitacion_list")

    def form_valid(self, form):
        messages.success(self.request, "Habitacion creada correctamente.", extra_tags="alert alert-success")
        return super().form_valid(form)
    
    def test_func(self):
        """ Devuelve True si el usuario tiene permiso."""
        return self.request.user.has_perm('hotel.add_habitacion')

class HabitacionDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Habitacion
    template_name = "hotel/confirm_delete.html"
    success_url = reverse_lazy("hotel:habitacion_list")

    def get_success_url(self):
            messages.success(self.request, "Habitacion eliminada correctamente.", extra_tags="alert alert-danger")
            return super().get_success_url()
    def test_func(self):
        """ Devuelve True si el usuario tiene permiso."""
        return self.request.user.has_perm('hotel.delete_habitacion')


class HabitacionUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Habitacion
    success_url = reverse_lazy("hotel:habitacion_list")
    form_class = forms.HabitacionForm

    def form_valid(self, form):
        messages.success(self.request, "Habitacion actualizada correctamente.", extra_tags="alert alert-success")
        return super().form_valid(form)

    def test_func(self):
        """ Devuelve True si el usuario tiene permiso."""
        return self.request.user.has_perm('hotel.change_habitacion')


# Reserva

class ReservaDetail(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = models.Reserva
    def test_func(self):
        """Determina el acceso a la vista, devuelve True si el usuario es el cliente o si es personal del staff, False de lo contrario."""
        reserva = self.get_object()
        return reserva.cliente == self.request.user or self.request.user.is_staff

class ReservaList(LoginRequiredMixin, ListView):
    model = models.Reserva
    def get_queryset(self):
        """Si el usuario no es un miembro del staff, muestra solo
        objetos que pertenecen al usuario que realiza la solicitud."""
        queryset = super().get_queryset()
        if not self.request.user.is_staff:
            queryset = queryset.filter(cliente=self.request.user)
        if self.request.GET.get("consulta"):
            query = self.request.GET.get("consulta")
            if self.request.user.is_staff:
                queryset = queryset.filter(cliente__username__icontains=query)
            else:
                queryset = queryset.filter(cliente=self.request.user, cliente__username__icontains=query)
        return queryset

class ReservaCreateView(LoginRequiredMixin, CreateView):
    model = models.Reserva
    form_class = forms.ReservaForm
    success_url = reverse_lazy("hotel:reserva_list")
    
    def form_valid(self, form):
        form.instance.cliente = self.request.user
        messages.success(self.request, "Reserva creada correctamente.", extra_tags="alert alert-success")
        return super().form_valid(form)

class ReservaDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Reserva
    template_name = "hotel/confirm_delete.html"
    success_url = reverse_lazy("hotel:reserva_list")

    def get_success_url(self):
            messages.success(self.request, "Reserva eliminada correctamente.", extra_tags="alert alert-danger")
            return super().get_success_url()
    
    def test_func(self):
        """Determina el acceso a la vista, devuelve True si el usuario autenticado es el cliente o si tiene permiso para eliminar la reserva."""
        reserva = self.get_object()
        return reserva.cliente == self.request.user or self.request.user.has_perm('hotel.delete_reserva')
    
class ReservaUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Reserva
    success_url = reverse_lazy("hotel:reserva_list")
    form_class = forms.ReservaForm

    def form_valid(self, form):
        messages.success(self.request, "Reserva actualizada correctamente.", extra_tags="alert alert-success")
        return super().form_valid(form)
    
    def test_func(self):
        """Determina el acceso a la vista, devuelve True si el usuario autenticado es el cliente o si tiene permiso para modificar la reserva."""
        reserva = self.get_object()
        return reserva.cliente == self.request.user or self.request.user.has_perm('hotel.change_reserva')
    
