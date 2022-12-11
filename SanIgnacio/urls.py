"""SanIgnacio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from landing import views
from usuario.views import singin,singout,signup,perfil,borrarPerfil
from servicios.views import listaPacientes,agregarControl,historial,seguridad,miPagos,miResidente,miSolicitud
from administracion.views import peticiones,pDetalle,admins,clientes,medicos,agregarCliente,modificarCliente,borrarUsuario,cambiarContra

urlpatterns = [
    ###Landing
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('nosotros/',views.nosotros, name='nosotros'),
    path('contacto/',views.contacto, name='contacto'),
    path('servicios/',views.servicios, name='servicios'),
    ###Usuario
    path('login/',singin, name='login'),
    path('logout/',singout, name='logout'),
    path('registro/',signup, name='registro'),
    path('perfil/',perfil, name='perfil'),
    ##Servicios
    path('perfil/pacientes/',listaPacientes, name='listaPacientes'),
    path('perfil/pacientes/agregarControl/<int:pk>',agregarControl, name='agregarControl'),
    path('perfil/pacientes/historial/<int:pk>',historial, name='historial'),
    path('perfil/seguridad/',seguridad, name='seguridad'),
    path('perfil/miPagos/',miPagos, name='miPagos'),
    path('perfil/delete/',borrarPerfil, name='borrarUsuario'),
    path('perfil/miResidente/',miResidente, name='miResidente'),
    path('perfil/miResidente/solicitud',miSolicitud, name='miSolicitud'),


    ##Administracion
    path('perfil/peticiones/',peticiones, name='peticiones'),
    path('perfil/peticiones/detalles/<pk>',pDetalle, name='detalle'),

    path('perfil/clientes/',clientes, name='clientes'),
    path('perfil/clientes/agregar/',agregarCliente, name='agregarCliente'),
    path('perfil/clientes/modificar/<pk>',modificarCliente, name='modificarCliente'),
    path('perfil/usuarios/borrar/<pk>',borrarUsuario, name='borrarUsuario'),
    path('perfil/usuarios/cambiarContrasenia/<pk>',cambiarContra, name='cambiarContra'),




    path('perfil/medicos/',medicos, name='medicos'),
    path('perfil/administradores/',admins, name='admins'),

]
