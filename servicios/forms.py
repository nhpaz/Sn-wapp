from django import forms
from usuario.models import Control_medico


class ControlForm(forms.ModelForm):
    
    class Meta:
        model = Control_medico
        fields = ("motivo_visita",'diagnostico','tratamiento')