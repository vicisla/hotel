from django.shortcuts import render
#from django.views.generic import View
from django.views.generic import FormView
#from .models import Consulta
from .forms import ConsultaForm
from django.contrib import messages


# Create your views here.
class ConsultaFormView(FormView):
    form_class = ConsultaForm
    template_name = 'home/index.html'
    success_url = '/'

    def form_valid(self, form):
        form.save()
        form.send_email()
        messages.success(self.request, "Mensaje enviado correctamente. Pronto nos pondremos en contacto con usted.", extra_tags="alert alert-success")
        return super().form_valid(form)
    
