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
from usuario.views import singin,singout,signup,perfil
from servicios.views import listaResidentes,agregarControl,historial


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('nosotros/',views.nosotros, name='nosotros'),
    path('contacto/',views.contacto, name='contacto'),
    path('servicios/',views.servicios, name='servicios'),
    path('login/',singin, name='login'),
    path('logout/',singout, name='logout'),
    path('registro/',signup, name='registro'),
    path('perfil/',perfil, name='perfil'),
    path('perfil/pacientes/',listaResidentes, name='listaResidente'),
    path('perfil/pacientes/agregarControl/<int:pk>',agregarControl, name='agregarControl'),
    path('perfil/pacientes/historial/<int:pk>',historial, name='historial'),






    
    
]
