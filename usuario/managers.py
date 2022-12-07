from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class UsuarioManager(BaseUserManager):
    """
    En este modelmanager donde el email es el identificador unico para la autentificación
    de usuarios

    """
    def create_user(self,rut, email, password,**extra_fields):
        """
        Crea un usuario con el mail y contraseña dada.
        """
        if not email:
            raise ValueError(_('Debe de tener email'))
        email = self.normalize_email(email)
        usuario = self.model(rut = rut, email=email,  **extra_fields)
        usuario.set_password(password)
        usuario.save()
        return usuario

    def create_superuser(self, rut,email, password, **extra_fields):
        """
        Crea un SuperUser con el email y contraseña dada.
        """
        extra_fields.setdefault('is_cliente',False)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser debe tener is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser debe tener is_superuser=True.'))
        return self.create_user(rut,email, password, **extra_fields)