from django.shortcuts import render,redirect
from usuario.models import Residente, Control_medico, PeticionResidente
from .forms import ControlForm,NuevaContraForm
from usuario.forms import ResidenteForm
# Create your views here.

### modulos compartidos
def seguridad(request):
    
    if request.method == 'GET':
        form = NuevaContraForm(user=request.user)
    
        return render(request,'templatesServicios/seguridad.html',{'form':form})
    
    else:
        
        form = NuevaContraForm(request.user,request.POST)
        print(form)
        
        if form.is_valid():
            form.save()
            
            return redirect('perfil')
        else:
            

            
            return render(request,'templatesServicios/seguridad.html',{'form':form,'Cerror':True})
        
        
### Modulos medico
def listaPacientes(request):
    if request.method == 'GET':
        residenteData = Residente.objects.all()
        
        
        
        return render(request,'templatesServicios/listaPacientes.html',{'residenteData':residenteData})

    else:
        residenteData = Residente.objects.all()

        return render(request,'templatesServicios/listaPacientes.html',{'residenteData':residenteData})

def agregarControl(request,pk):
    
    if request.method =='GET':
    
        residente = Residente.objects.get(pk=pk)
        control_form = ControlForm
        
        return render(request,'templatesServicios/pacienteControl.html',{'residente': residente ,'form':control_form})
    

    if request.method =='POST':
        
        control_form = ControlForm(request.POST)
        
        if control_form.is_valid:
            
            control = control_form.save(commit=False)
            control.residente_id = pk
            control.medico_id = request.user.medico.id
            control.save()
            return redirect('listaPacientes')
        
def historial(request,pk):
    
    if request.method =='GET':
        
        residente = Residente.objects.get(id=pk)
        controles= Control_medico.objects.filter(residente_id=pk)
        

        return render(request,'templatesServicios/pacienteHistorial.html',{'residente': residente ,'controles':controles})
    
### Modulos Clientes

def miResidente(request):
    usuario_actual = request.user

    if request.method == 'GET':
        residenteData = Residente.objects.filter(cliente_id = usuario_actual.cliente.id)

        return render(request,'templatesServicios/miResidente.html',{'residenteData':residenteData})
    else:
        return redirect('miSolicitud')
    
def miSolicitud(request):
    usuario_actual= request.user
    if request.method == 'GET':
        form = ResidenteForm
        
        return render(request,'templatesServicios\miSolicitud.html',{'form':form})
    
        
    else:
        form = ResidenteForm(request.POST)
        print(request.POST)
        if form.is_valid():
            residente = form.save(commit=False)
            residente.cliente_id = usuario_actual.id
            residente.save()
            
            residenteGuardado= Residente.objects.get(rut=request.POST['rut'])
            print(residenteGuardado.id)
            peticion = PeticionResidente()
            peticion.cliente_id = usuario_actual.cliente.id
            peticion.residente_id = residenteGuardado.id
            peticion.save()
            return redirect('miResidente')

        else:
            return render(request,'templatesServicios\miSolicitud.html',{'form':form,'Cerror':True})

            
        

    
    
    

def miPagos(request):
    
    return render(request,'templatesServicios/miPagos.html')

        
        
    
    




    

    
    
    
    
