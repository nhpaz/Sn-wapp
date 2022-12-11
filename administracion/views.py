from django.shortcuts import render ,redirect
from usuario.models import PeticionResidente, Usuario,Cliente,Medico
from usuario.forms import UsuarioForm,ClienteForm
from servicios.forms import NuevaContraForm
# Create your views here.

###PETICIONES###

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

###MODULOS COMPARTIDOS###
def cambiarContra(request,pk):
    usuario = Usuario.objects.get(id=pk)

    
    if request.method == 'GET':
        form = NuevaContraForm(user=usuario)
    
        return render(request,'templatesServicios/seguridad.html',{'form':form})
    
    else:
        form = NuevaContraForm(usuario,request.POST)        
        if form.is_valid():
            form.save()
            if usuario.is_admin:
                return redirect('perfil')
            if usuario.is_cliente:
                return redirect('clientes')
            if usuario.is_medico:
                return redirect('perfil')
        else:
            return render(request,'templatesAdministracion/cambiarContraCliente.html',{'form':form,'Cerror':True})


###CRUD CLIENTES###

def clientes(request):
    
    if request.method == 'GET':
    
        clientesData = Cliente.objects.all()
    
        return render(request,'templatesAdministracion/listaClientes.html',{'clientesData':clientesData})
    else:
        
        return redirect('perfil')
    
def agregarCliente(request):

    if request.method == 'GET':
        cform = ClienteForm
        uform = UsuarioForm
        
        return render(request,'templatesAdministracion/agregarCliente.html',{'cform':cform,'uform':uform})
        
    else:
        cform = ClienteForm(request.POST)
        uform = UsuarioForm(request.POST)
        print(uform)
        print(cform)
        
        
        if cform.is_valid() and uform.is_valid():
            usuario = uform.save(commit=False)
            usuario.save()
            print(request.POST)

            usuario.cliente.direccion = cform.cleaned_data.get('direccion')
            usuario.cliente.save()
            return redirect('clientes')
            
        else:
            uform = UsuarioForm(request.POST)
            cform =  ClienteForm(request.POST)
            
        return render(request,'templatesAdministracion/agregarCliente.html',{'cform':cform,'uform':uform})

def cambiarContraCliente(request,pk):
    
    if request.method == 'GET':
        return render(request,'templatesAdministracion/cambiarContraCliente.html')

def borrarUsuario(request,pk):
    if request.method == 'POST':
        Usuario = Usuario.objects.get(pk=pk)
        Usuario.delete()
        
        return redirect('clientes')
    else:
        return render(request,'templatesAdministracion/borrarCliente.html')
    
def modificarCliente(request,pk):
    
    if request.method == 'GET':
    
        cData = Cliente.objects.get(pk=pk)
    
        return render(request,'templatesAdministracion/modificarCliente.html',{'cData':cData})
    
    else:
        try:
            cliente = Cliente.objects.get(pk=pk)
            cliente.usuario.first_name = request.POST['first_name']
            cliente.usuario.last_name = request.POST['last_name']
            cliente.usuario.telefono = request.POST['telefono']
            cliente.usuario.email = request.POST['email']            
            cliente.direccion = request.POST['direccion']
            cliente.usuario.save()
            cliente.save()
            return redirect('clientes')

        except:
            return render(request,'templatesAdministracion/modificarCliente.html',{'error':'Porfavor, rellene los campos requeridos'})

###CRUD MEDICOS###

def medicos(request):
    
    if request.method == 'GET':
    
        clientesData = Cliente.objects.all()
    
        return render(request,'templatesAdministracion/listaMedicos.html',{'clientesData':clientesData})
    else:
        
        return redirect('perfil')
###CRUD ADMINISTRADORES###

def admins(request):
    
    if request.method == 'GET':
    
        clientesData = Cliente.objects.all()
    
        return render(request,'templatesAdministracion/listaAdmin.html',{'clientesData':clientesData})
    else:
        
        return redirect('perfil')
    
    



    
    
    
    