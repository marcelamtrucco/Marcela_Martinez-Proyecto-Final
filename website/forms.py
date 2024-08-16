from django import forms
from website.models import Reserva_Clase

class SociosFormulario(forms.Form):
    nombre=forms.CharField(max_length=30)
    apellido=forms.CharField(max_length=30)
    email=forms.EmailField(max_length=30)
    telefono=forms.CharField(max_length=50)

class Reserva_Form(forms.ModelForm):
    class Meta:
        model = Reserva_Clase
        fields = [
            'user',
            'id_socio',
            'clase',
            'turno',
            'fecha',
            ]
        labels={
            'user':'USUARIO',
            'id_socio': 'INDICAR NUMERO DE SOCIO',
            'clase':'SELECCIONAR LA CLASE',
            'turno':'SELECCIONAR EL HORARIO',
            'fecha':'SELECCIONAR SEMANA',
            }
        widgets={
            'user': forms.Select(attrs={'class':'form-control'}),
            'id_socio':forms.Select(attrs={'class':'form-control'}),
            'clase':forms.Select(attrs={'class':'form-control'}),
            'turno': forms.Select(attrs={'class':'TIMEBLOCK_CHOICES'}),
            'fecha': forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
            }    
        
class YogaForm(forms.Form):
    name = forms.CharField(max_length=50, required=False, empty_value=None)   