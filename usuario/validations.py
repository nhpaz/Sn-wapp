from django.core.exceptions import ValidationError
from rut_chile import rut_chile


def ValidacionRut(rut):
    
    try:
        if rut_chile.is_valid_rut(rut):
            return rut
        
        else:
            raise ValidationError('El rut no es valido')
    except:
        raise ValidationError('El rut no es valido')