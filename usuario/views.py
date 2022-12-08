from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout, authenticate
from django.shortcuts import redirect
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Usuario,Residente
from .forms import UsuarioForm,ClienteForm,ResidenteForm

import time




# Create your views here.



def singin (request):
    if request.method == "GET":
        form = AuthenticationForm
        return render(request,'templatesUsuario/login.html',{'form':form})
    
    else:

        user= authenticate(request, email=request.POST['username'],password= request.POST['password'])  
        if user is None:
            return render(request,'templatesUsuario/login.html',{'error': 'hay un error'})
        else:
            login(request,user)
            return redirect('perfil')
            
            
def singout(request):
    logout(request)
    return redirect('home')


def signup(request):
    if request.method == 'GET':
        usuario_form = UsuarioForm
        cliente_form =  ClienteForm 
        
        
        return render(request, 'templatesUsuario/registro.html',{'usuario_form':usuario_form,'cliente_form':cliente_form})
    else:

        usuario_form = UsuarioForm(request.POST)
        cliente_form = ClienteForm(request.POST)
        print(usuario_form.is_valid())
        print(cliente_form.is_valid())
        
        if usuario_form.is_valid() and cliente_form.is_valid():
            usuario = usuario_form.save(commit=False)
            usuario.save()
            print(request.POST)

            usuario.cliente.direccion = cliente_form.cleaned_data.get('direccion')
            usuario.cliente.save()
            login(request,usuario)
            messages.success(request, 'El registro se ha realizado con éxito')
            time.sleep(2)
            return redirect('perfil')
            
        else:
            usuario_form = UsuarioForm(request.POST)
            cliente_form =  ClienteForm(request.POST)
            
        return render(request, 'templatesUsuario/registro.html',{'usuario_form':usuario_form,'cliente_form':cliente_form})
    
    
@login_required
def perfil(request):
    usuario_actual = request.user


    if request.method == 'GET':

        return render(request,'templatesUsuario/perfil.html')
    
    else:
        
        if usuario_actual.is_cliente:
            try:
                usuario = Usuario.objects.get(pk=usuario_actual.id)
                usuario.first_name = request.POST['first_name']
                usuario.last_name = request.POST['last_name']
                usuario.telefono = request.POST['telefono']
                usuario.email = request.POST['email']
                
                usuario.cliente.direccion = request.POST['direccion']
                usuario.cliente.save()
                usuario.save()
                return redirect('perfil')

            except:
                return render(request,'templatesUsuario/perfil.html',{'error':'Porfavor, rellene los campos requeridos'})

                
            
        else:
            usuario = Usuario.objects.get(pk=usuario_actual.id)
            usuario.first_name = request.POST['first_name']
            usuario.last_name = request.POST['last_name']
            usuario.telefono = request.POST['telefono']
            usuario.email = request.POST['email']
            usuario.save()
            
            return redirect('perfil')
        
        
def borrarPerfil(request):
    usuario_actual = request.user

    if request.method == 'POST':
        logout(request)

        usuario = Usuario.objects.get(pk=usuario_actual.id)
        usuario.delete()
        return redirect('home')
    else:
        return render(request,'templatesUsuario/borrarPerfil.html')

    
        
        

        
        
        




            
            
        
            
            
'''def perfil(request):
    
    if request.method == 'GET':
        usuario_actual = request.user

        residenteForm = ResidenteForm 
        if usuario_actual.is_cliente:
            residenteData = Residente.objects.filter(cliente_id = usuario_actual.cliente.id)

            
            return render(request,'templatesUsuario/perfil.html',{'residenteForm':residenteForm,'residenteData':residenteData})
        else:
            return render(request,'templatesUsuario/perfil.html',{'residenteForm':residenteForm})

            
    
    else:
        usuario_actual = request.user
        usuario_actual_id = usuario_actual.cliente.id

        residenteForm = ResidenteForm(request.POST)
        print(residenteForm.is_valid())
        residenteData = Residente.objects.filter(cliente_id = usuario_actual.cliente.id)

        
        if residenteForm.is_valid:
            residente = residenteForm.save(commit=False)
            residente.cliente_id = usuario_actual_id

            residente.save()
            
            return render(request,'templatesUsuario/perfil.html',{'residenteForm':residenteForm,'residenteData':residenteData})
            
        else:
            
            return render(request,'templatesUsuario/perfil.html',{'error':'formulario no valido'})
            '''