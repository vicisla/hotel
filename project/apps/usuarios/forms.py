from django import forms
from .models import InfoUsuario


class InfoUsuarioForm(forms.ModelForm):
    nacimiento = forms.DateField(input_formats=['%d/%m/%Y'], widget=forms.DateInput(format='%d/%m/%Y', attrs={"placeholder": "DD/MM/YYYY"}))
    class Meta:
        model = InfoUsuario
        fields = ['avatar', 'nacimiento', 'pais', 'provincia', 'ciudad', 'domicilio', 'codigo_postal', 'telefono', 'dni', 'cuit']


