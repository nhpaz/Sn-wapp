from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages


# Create your views here.

def home (request):
    return render(request,'templatesLanding/index.html')

def nosotros (request):
    return render(request,'templatesLanding/nosotros.html')

def contacto (request):
        if request.method == "POST":
            nombre = request.POST ['nombre']
            apellido = request.POST ['apellido']
            telefono = request.POST ['telefono']
            email = request.POST ['email']
            tipo_consulta = request.POST ['tipo_consulta']
            message = request.POST ['message']
            email_from = settings.EMAIL_HOST_USER
        
        
            send_mail(tipo_consulta,'Nombre:'+" "+nombre+'\nApellido:'+" "+apellido+'\nTelefono:'+" "+telefono+'\nCorreo Electrónico:'+" "+email+'\nMensaje:'+" "+message,email_from,[email_from])
            messages.success(request, 'El mensaje se ha enviado con éxito')
            return redirect('contacto')
        
        else:
            return render(request,'templatesLanding/contacto.html')

def servicios (request):
    return render(request,'templatesLanding/servicios.html')



