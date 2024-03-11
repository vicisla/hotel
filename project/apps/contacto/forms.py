from django import forms
from .models import Consulta
from captcha.fields import CaptchaField

class ConsultaForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Consulta
        fields = [
            "nombre", "apellido", "email", "mensaje"
        ]
    
    def send_email(self):
        nombre = self.cleaned_data["nombre"]
        apellido = self.cleaned_data["apellido"]
        email = self.cleaned_data["email"]
        mensaje = self.cleaned_data["mensaje"]
        # Agregar logica envio de email 
        