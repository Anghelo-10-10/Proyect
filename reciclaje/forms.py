from django import forms
from .models import PuntoAlmacenamiento
from django.db import connection 

class PuntoAlmacenamientoForm(forms.ModelForm):
    class Meta:
        model = PuntoAlmacenamiento
        fields = ['nombre', 'direccion', 'ciudad', 'telefono', 'email', 'horario_apertura', 'capacidad_total']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'direccion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Dirección'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ciudad'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'}),
            'horario_apertura': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Horario de apertura'}),
            'capacidad_total': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Capacidad total'}),
        }
