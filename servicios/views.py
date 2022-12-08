from django.shortcuts import render,redirect
from usuario.models import Residente, Control_medico
from .forms import ControlForm

# Create your views here.


def listaResidentes(request):
    if request.method == 'GET':
        residenteData = Residente.objects.all()
        
        
        
        return render(request,'templatesServicios/listaResidentes.html',{'residenteData':residenteData})

    else:
        residenteData = Residente.objects.all()

        return render(request,'templatesServicios/listaResidentes.html',{'residenteData':residenteData})
    
    
    
def agregarControl(request,pk):
    
    if request.method =='GET':
    
        residente = Residente.objects.get(id=pk)
        control_form = ControlForm
        
        print(request.user.id)

        return render(request,'templatesServicios/residenteControl.html',{'residente': residente ,'form':control_form})
    

    if request.method =='POST':
        
        control_form = ControlForm(request.POST)
        
        if control_form.is_valid:
            
            control = control_form.save(commit=False)
            control.residente_id = pk
            control.medico_id = request.user.id
            control.save()
            return redirect('listaResidente')
        
def historial(request,pk):
    
    if request.method =='GET':
        
        residente = Residente.objects.get(id=pk)
        controles= Control_medico.objects.filter(residente_id=pk)
        

        return render(request,'templatesServicios/residenteHistorial.html',{'residente': residente ,'controles':controles})
    
def seguridad(request):
    
    return render(request,'templatesServicios/seguridad.html')


def Pagos(request):
    
    return render(request,'templatesServicios/pagos.html')

        
        
    
    




    

    
    
    
    
