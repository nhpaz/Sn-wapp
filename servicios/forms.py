from django import forms
from django.contrib.auth.forms import SetPasswordForm
from usuario.models import Control_medico,Usuario


class ControlForm(forms.ModelForm):
    
    class Meta:
        model = Control_medico
        fields = ("motivo_visita",'diagnostico','tratamiento')
        
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
        
