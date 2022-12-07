from .models import Usuario,Medico,Cliente,Residente
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm


class UsuarioForm(UserCreationForm):
    
    class Meta:
        model = Usuario
        fields = ("rut","first_name",'last_name','email')

class MedicoForm(forms.ModelForm):
    
    class Meta:
        model = Medico
        fields = ("especialidad",)


class ClienteForm(forms.ModelForm):
    
    class Meta:
        model = Cliente
        fields = ("direccion",) 
        
class ResidenteForm(forms.ModelForm):
    class Meta:
        model = Residente
        fields = ('rut','nombre','apellido')
