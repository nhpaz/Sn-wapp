from django.shortcuts import render ,redirect
from usuario.models import PeticionResidente
# Create your views here.

def peticiones(request):
    
    if request.method == 'GET':
        
        pData = PeticionResidente.objects.all()
        
        
        return render(request,'templatesAdministracion\peticiones.html',{'pData':pData})
    
def pDetalle(request,pk):
    
    if request.method == 'GET':
        pData = PeticionResidente.objects.get(id=pk)

        
        return render(request,'templatesAdministracion\pDetalle.html',{'pData':pData})
    
    else:
        peticion = PeticionResidente.objects.get(id=pk)
        peticion.esta_aceptado = True;
        peticion.residente.esta_activo = True;
        peticion.residente.save() 
        peticion.save()
        
        return redirect('peticiones')
        

    
    
    
    
    