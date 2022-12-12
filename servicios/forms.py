from django import forms
from django.contrib.auth.forms import SetPasswordForm
from usuario.models import Control_medico,Usuario
from django.forms import TextInput,Textarea,NumberInput



class ControlForm(forms.ModelForm):
    
    class Meta:
        model = Control_medico
        fields = ("motivo_visita",'diagnostico','tratamiento')
        widgets = {
            'motivo_visita': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Motivo de visita',
                }),
            'diagnostico': Textarea(attrs={
                'class': "form-control form-control-sm",
                'rows' : '4',
                'placeholder': 'Diagnostico'
            }),
            'tratamiento': Textarea(attrs={
                'class': "form-control form-control-sm",
                'rows' : '4',
                'placeholder': 'Tratamiento'
            })
            }
        
class NuevaContraForm(SetPasswordForm):
    new_password1 = forms.CharField(
    widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "class": "form-control",'placeholder':'Nueva contraseña'}),
    )
    new_password2 = forms.CharField(
    widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "class": "form-control",'placeholder':'Confirmar nueva contraseña'}),
    )
    
    class Meta:
        model = Usuario
        fields = ("new_password1","new_password2")
        
