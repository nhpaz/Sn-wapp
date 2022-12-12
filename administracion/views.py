from django.shortcuts import render ,redirect
from usuario.models import PeticionResidente, Usuario,Cliente,Medico,Admin,Residente
from usuario.forms import UsuarioForm,ClienteForm,MedicoForm,AdminForm,ResidenteForm,ResidenteFormUpdate
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
    
        return render(request,'templatesAdministracion/cambiarContra.html',{'form':form})
    
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
            return render(request,'templatesAdministracion/cambiarContra.html',{'form':form,'Cerror':True})

def borrar(request,pk):
    if request.method == 'POST':
        Usuario = Usuario.objects.get(pk=pk)
        Usuario.delete()
        
        return redirect('clientes')
    else:
        return render(request,'templatesAdministracion/borrar.html')

def modificar(request,pk):
    
    if request.method == 'GET':
    
        uData = Usuario.objects.get(pk=pk)
        print(request.session)
    
        return render(request,'templatesAdministracion/modificar.html',{'uData':uData})
    
    else:
        usuario = Usuario.objects.get(pk=pk)
        if usuario.is_cliente:
            try:
                usuario.first_name = request.POST['first_name']
                usuario.last_name = request.POST['last_name']
                usuario.telefono = request.POST['telefono']
                usuario.email = request.POST['email']            
                usuario.cliente.direccion = request.POST['direccion']
                usuario.cliente.save()
                usuario.save()
                return redirect('clientes')

            except:
                return render(request,'templatesAdministracion/modificar.html',{'error':'Porfavor, rellene los campos requeridos','uData':usuario})
        if usuario.is_medico:
            try:
                usuario.first_name = request.POST['first_name']
                usuario.last_name = request.POST['last_name']
                usuario.telefono = request.POST['telefono']
                usuario.email = request.POST['email']            
                usuario.medico.especialidad = request.POST['especialidad']
                usuario.medico.sueldo = request.POST['sueldo']
                usuario.medico.save()
                usuario.save()
                return redirect('medicos')

            except:
                return render(request,'templatesAdministracion/modificar.html',{'error':'Porfavor, rellene los campos requeridos','uData':usuario})
        if usuario.is_admin:
            try:
                usuario.first_name = request.POST['first_name']
                usuario.last_name = request.POST['last_name']
                usuario.telefono = request.POST['telefono']
                usuario.email = request.POST['email']            
                usuario.admin.sueldo = request.POST['sueldo']
                print(request.POST)
                usuario.admin.save()
                usuario.save()
                return redirect('admins')

            except:
                print(request.POST)

                return render(request,'templatesAdministracion/modificar.html',{'error':'Porfavor, rellene los campos requeridos','uData':usuario})

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

def agregarResidente(request,pk):
    if request.method == 'GET':
        form = ResidenteForm
        
        
        return render(request,'templatesAdministracion/agregarResidente.html',{'form':form})
        
    else:
        form = ResidenteForm(request.POST)
        if form.is_valid():
            residente = form.save(commit=False)
            residente.esta_activo = True
            residente.cliente_id = pk
            
            residente.save()
            return render(request,'templatesAdministracion/agregarResidente.html',{'form':form ,'exito':'Exito'})
        else:
            return render(request,'templatesAdministracion/agregarResidente.html',{'form':form})

#Residente
def residentes(request):
    if request.method == 'GET':
        residenteData = Residente.objects.all()
        return render(request,'templatesAdministracion/ListaResidente.html',{'residenteData':residenteData})

def modificarResidente(request,pk):
    reData = Residente.objects.get(pk=pk)
    if request.method == 'GET':

        form = ResidenteFormUpdate(instance=reData)
        return render(request,'templatesAdministracion/modificarResidente.html',{'reData':reData,'form':form})

    else:

        residente = ResidenteFormUpdate(request.POST, instance=reData)
        print
        if residente.is_valid():
            residente.save()
            return redirect('residentes')
        else:
            return render(request,'templatesAdministracion/modificarResidente.html',{'reData':reData,'form':form})

    
    

###CRUD MEDICOS###

def medicos(request):
    
    if request.method == 'GET':
    
        medicosData = Medico.objects.all()
    
        return render(request,'templatesAdministracion/listaMedicos.html',{'medicosData':medicosData})
    else:
        
        return redirect('perfil')

def agregarMedico(request):
    
    if request.method == 'GET':
        mform = MedicoForm
        uform = UsuarioForm

        
        return render(request,'templatesAdministracion/agregarMedico.html',{'uform':uform,'mform':mform})
        
    else:
        mform = MedicoForm(request.POST)
        uform = UsuarioForm(request.POST)

        
        
        if mform.is_valid() and uform.is_valid():
            usuario = uform.save(commit=False)
            usuario.is_medico = True
            usuario.is_cliente = False
            usuario.save()
            print(request.POST)

            usuario.medico.especialidad = mform.cleaned_data.get('especialidad')
            usuario.medico.sueldo = mform.cleaned_data.get('sueldo')

            usuario.medico.save()
            return redirect('medicos')
            
        else:
            mform = MedicoForm(request.POST)
            uform = UsuarioForm(request.POST)

            
        return render(request,'templatesAdministracion/agregarMedico.html',{'mform':mform,'uform':uform})


###CRUD ADMINISTRADORES###

def admins(request):
    
    if request.method == 'GET':
    
        adminsData = Admin.objects.all()
    
        return render(request,'templatesAdministracion/listaAdmin.html',{'adminsData':adminsData})
    else:
        
        return redirect('perfil')
    
def agregarAdmin(request):
    
    if request.method == 'GET':
        aform = AdminForm
        uform = UsuarioForm

        
        return render(request,'templatesAdministracion/agregarAdmin.html',{'uform':uform,'aform':aform})
        
    else:
        aform = AdminForm(request.POST)
        uform = UsuarioForm(request.POST)

        
        
        if aform.is_valid() and uform.is_valid():
            usuario = uform.save(commit=False)
            usuario.is_cliente = False
            usuario.is_admin = True
            usuario.save()
            usuario.admin.sueldo = aform.cleaned_data.get('sueldo')
            usuario.admin.save()
            return redirect('admins')
            
        else:
            aform = AdminForm(request.POST)
            uform = UsuarioForm(request.POST)

            
        return render(request,'templatesAdministracion/agregarAdmin.html',{'uform':uform,'aform':aform})



    
    
    
    