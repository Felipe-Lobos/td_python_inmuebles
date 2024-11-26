from datetime import timezone
from django.contrib import admin
from .models import Inmueble, Usuario, Comuna, Region,Foto
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth import get_user_model
# Register your models here.

# admin.site.register(Inmueble)
admin.site.register(Usuario)
admin.site.register(Comuna)
admin.site.register(Region)
admin.site.register(Foto)




@admin.register(Inmueble)
class InmuebleAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'precio_mensual')
    search_fields = ('nombre', 'direccion')
    list_filter = ('precio_mensual', 'comuna')
    # readonly_fields = ('fecha_creacion', 'ultima_modificacion')
    
    # def save_model(self, request, obj, form, change):
    #     if change:
    #         obj.ultima_modificacion = timezone.now()
    #     else:
    #         obj.fecha_creacion = timezone.now()
    #         obj.save()
    
