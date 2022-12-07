from .models import Usuario,Medico,Cliente,Admin
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=Usuario)
def crear_cliente(sender, instance, created, **kwargs):
    print('****', created)
    print('-----',instance.is_cliente)
    if instance.is_cliente == True:
        Cliente.objects.get_or_create(usuario = instance)
    if instance.is_medico == True:
        Medico.objects.get_or_create(usuario = instance)            
    else:
        Admin.objects.get_or_create(usuario = instance)
                
        


@receiver(post_save, sender=Usuario)
def guardar_cliente( sender,instance, **kwargs):
    print('_-----')
    if  instance.is_cliente:
        instance.cliente.save()
        print('-usuario cliente-')
        
    if  instance.is_medico:
        instance.medico.save()
        print('-usuario medico-')

    else:
        instance.admin.save()
        print('-usuario admin-')

        
        

        
''' @receiver(post_save,sender = Usuario)
def crear_cliente(sender,instance,created,**kwargs):
    if created:
        Cliente.objects.create(usuario=instance)

@receiver(post_save,sender = Usuario)
def guardar_cliente(sender,instance,**kwargs):
    instance.cliente.save()
     '''
            