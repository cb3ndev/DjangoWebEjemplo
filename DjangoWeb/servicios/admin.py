#eSTA APP se hizo despues de la prinicpal proyectoweb ver esa primero

from django.contrib import admin
from .models import Servicio


#En el modelo Servicios cuando se ve en el pan el de admin, no aprecen normalmente los campos de created o updated.
#Por lo que deberemos crear este otra clase con created y updated y ponerlas como read_only
class ServicioAdmin(admin.ModelAdmin):
	readonly_fields=('created','updated')


admin.site.register(Servicio, ServicioAdmin)

# Register your models here.
