from .models import Usuario,Medico,Cliente,Residente,Admin,Tipo_pago,Factura,DetalleFactura
from django import forms
from django.forms import TextInput,Textarea,NumberInput
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm


## Pagos

class FacturaForm(forms.ModelForm):
    
    class Meta:
        model = Factura
        fields = ("estado",)


class TipoPagoForm(forms.ModelForm):
    
    class Meta:
        model = Tipo_pago
        fields = ("tipo",)
        widgets = {
            'tipo': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Tipo',
                })}
class DetalleFacturaForm(forms.ModelForm):
    
    class Meta:
        model = DetalleFactura
        fields = ('servicio','tipo_pago')



##
class UsuarioForm(UserCreationForm):
    password1 = forms.CharField(
    label="Contraseña",
    widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "class": "form-control",'placeholder':'Nueva contraseña'}),
    )
    
    password2 = forms.CharField(
    label="Confirma contraseña",
    widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "class": "form-control",'placeholder':'Confirmar nueva contraseña'}),
    )
    first_name = forms.CharField(
    label= "Nombre",
    widget=TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Nombre',
                'required pattern':"[a-zA-Z]+(?:\s[a-zA-Z]+)?",
                'title':"Solamente Letras",
                })
    )
    
    last_name = forms.CharField(
    label="Apellidos",
    widget= TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Apellidos',
                'required pattern':"[a-zA-Z]+(?:\s[a-zA-Z]+)?",
            })
    )
        
    
    class Meta:
        model = Usuario
        fields = ("rut","first_name",'last_name','email','telefono')

        widgets = {

            'rut': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'xxxxxxxx-x',
            }),
   
            'email': TextInput(attrs={
                'class': "form-control form-control",
                'placeholder': 'Correo electronico',
                'type':"email",
            }),
   
            'telefono': NumberInput(attrs={
                'class': "form-control form-control",
                'placeholder': 'xxxx-xxx-xxx',
                'required pattern':'[0-9]{9}',
                'title':"ejemplo: 123456789",

            })

            }
        
        
        
class MedicoForm(forms.ModelForm):
    
    class Meta:
        model = Medico
        fields = ("especialidad","sueldo")
        widgets = {
            'especialidad': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Especialidad',
                }),
            'sueldo': NumberInput(attrs={
                'class': "form-control",
                'placeholder': 'Sueldo',
                })}

class ClienteForm(forms.ModelForm):
    
    class Meta:
        model = Cliente
        fields = ("direccion",) 
        widgets = {
            'direccion': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Dirección',
                })}
        
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

class ResidenteFormUpdate(forms.ModelForm):
    class Meta:
        model = Residente
        fields = ('nombre','apellido','enfermedad','medicamento')
        widgets = {
            'nombre': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Nombre',
                'required pattern':"[a-zA-Z]+(?:\s[a-zA-Z]+)?",
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


class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = ("sueldo",)
        widgets = {
            'sueldo': NumberInput(attrs={
                'class': "form-control",
                'placeholder': 'Sueldo',
                })}
        

        
        