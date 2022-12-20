from django.contrib import admin
from .models import Usuario,Medico,Residente,Control_medico,Cliente,PeticionResidente,Factura,DetalleFactura,Servicio,Tipo_pago
# Register your models here.

admin.site.register(Usuario)
admin.site.register(Cliente)
admin.site.register(Medico)
admin.site.register(Residente)
admin.site.register(Control_medico)
admin.site.register(PeticionResidente)
admin.site.register(Factura)
admin.site.register(DetalleFactura)
admin.site.register(Servicio)
admin.site.register(Tipo_pago)





