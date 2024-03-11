from django import forms
from . import models

class TipoHabitacionForm(forms.ModelForm):
    class Meta:
        model = models.TipoHabitacion
        fields = '__all__'
       

class HabitacionForm(forms.ModelForm):
    class Meta:
        model = models.Habitacion
        fields = '__all__'
        widgets = {
            "tipo": forms.Select(),
            "numero": forms.TextInput(),
            "precio_x_dia": forms.TextInput(),
            "disponible": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "imagen": forms.FileInput(),
            }

class ReservaForm(forms.ModelForm):
    fecha_entrada = forms.DateField(input_formats=['%d/%m/%Y'], widget=forms.DateInput(format='%d/%m/%Y', attrs={"placeholder": "DD/MM/YYYY"}))
    fecha_salida = forms.DateField(input_formats=['%d/%m/%Y'], widget=forms.DateInput(format='%d/%m/%Y', attrs={"placeholder": "DD/MM/YYYY"}))

    class Meta:
        model = models.Reserva
        fields = ['habitacion', 'fecha_entrada', 'fecha_salida']
    