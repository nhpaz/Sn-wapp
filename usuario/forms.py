from .models import Usuario,Medico,Cliente,Residente
from django import forms
from django.forms import TextInput,Textarea
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
        fields = ('rut','nombre','apellido','enfermedad','medicamento')
        widgets = {
            'nombre': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Nombre',
                'required pattern':"[a-zA-Z]+(?:\s[a-zA-Z]+)?",
                'title':"Solamente Letras",
                }),
            'rut': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Rut: xxxxxxxx-x',

                'title':"Solamente Letras",
            }),
            'apellido': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Apellidos',
                'required pattern':"[a-zA-Z]+(?:\s[a-zA-Z]+)?",
            }),
            'enfermedad': Textarea(attrs={
                'class': "form-control form-control-sm",
                'rows' : '4',
                'placeholder': 'Enfermedad'
            }),
            'medicamento': Textarea(attrs={
                'class': "form-control form-control-sm",
                'rows' : '4',
                'placeholder': 'Medicamentos'
            })
            }
        