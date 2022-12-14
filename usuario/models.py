from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.core.validators import RegexValidator

from .validations import ValidacionRut
from .managers import UsuarioManager

# Create your models here.



class Usuario(AbstractUser):
    username = None
    rut = models.CharField(max_length=12,unique=True,validators=[RegexValidator(regex='^[0-9]+-[0-9kK]{1}$',message='El rut debe de ser sin puntos y con guion'),ValidacionRut])
    
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(max_length=36)
    last_name = models.CharField(max_length=36)
    telefono = models.IntegerField(null=True)
    is_cliente = models.BooleanField(default=True)
    is_medico = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['rut']

    objects = UsuarioManager()

    def __str__(self):
        return self.rut+ " "+ self.first_name +" "+ self.last_name+" "
    
class Cliente(models.Model):
    usuario= models.OneToOneField(Usuario,null=True, on_delete=models.CASCADE,related_name='cliente')
    direccion = models.CharField(max_length=60)
    
    
class Medico(models.Model):
    usuario= models.OneToOneField(Usuario,null=True, on_delete=models.CASCADE,related_name='medico')
    sueldo = models.IntegerField(null=True)
    fecha_contrato = models.DateField(null= True)
    especialidad = models.CharField(max_length=5)
    
    
class Admin(models.Model):
    usuario= models.OneToOneField(Usuario,null=True, on_delete=models.CASCADE,related_name='admin')
    fecha_contrato = models.DateField(null=True)
    sueldo = models.IntegerField(null=True)    
    

    
    
class Residente(models.Model):
    rut = models.CharField(max_length=12, unique=True,validators=[RegexValidator(regex='^[0-9]+-[0-9kK]{1}$',message='El rut debe de ser sin puntos y con guion'),ValidacionRut])
    nombre = models.CharField(max_length=36)
    apellido = models.CharField(max_length=36)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE,related_name='residente')
    fecha_estadia = models.DateTimeField(default=timezone.now)
    enfermedad = models.TextField(null=True)
    medicamento = models.TextField(null=True)
    esta_activo = models.BooleanField(default=False)

    
    
class Control_medico(models.Model):
    motivo_visita= models.CharField(max_length=150)
    fecha_control= models.DateTimeField(default=timezone.now)
    diagnostico=models.TextField(max_length=300)
    tratamiento=models.TextField(max_length=300)
    residente = models.ForeignKey(Residente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico,on_delete=models.DO_NOTHING)

class PeticionResidente(models.Model):
    esta_aceptado = models.BooleanField(default=False)
    fecha_peticion= models.DateField(default=timezone.now)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE,related_name='cliente')
    residente = models.ForeignKey(Residente, on_delete=models.CASCADE) 


class Factura(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)
    estado = models.BooleanField(default= False)

class Tipo_pago(models.Model):
    tipo = models.CharField(max_length=50)
    def __str__(self):
        return self.tipo
    

class Servicio(models.Model):
    nombre = models.CharField(max_length=30) 
    precio= models.IntegerField()
    def __str__(self):
        return self.nombre + ' (Precio: '+str(self.precio) +')'
    
    
class DetalleFactura(models.Model):
    factura = models.OneToOneField(Factura, on_delete=models.CASCADE,related_name='detalle')
    fecha_creacion = models.DateField(default=timezone.now)
    tipo_pago = models.ForeignKey(Tipo_pago, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    


