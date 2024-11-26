from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import ValidationError
import uuid
from django.utils.timezone import now
from django.contrib.auth.models import Group
# Create your models here.

TIPO_USUARIO = [
    ('arrendador','Arrendador'),
    ('arrendatario','Arrendatario'),
    ('administrador','Administrador')
]
class Usuario(AbstractUser):
    nombres  = models.CharField(max_length=150, null=False, blank=False)
    apellidos = models.CharField(max_length=150, null=False, blank=False)
    rut = models.CharField(max_length=10, null=False, blank=False, unique=True)
    direccion = models.CharField(max_length=250, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    # email desde AbstracUser
    tipo_usuario = models.CharField(max_length=50, choices=TIPO_USUARIO, default='arrendatario')
    is_active = models.BooleanField(default=True, editable=False)
    deleted_at = models.DateTimeField(blank=True,null=True, editable=False)
    
    def delete(self, *args, **kwargs):
        self.is_active = False
        self.deleted_at = now()
        if self.inmuebles.exists():
            for inmueble in self.inmuebles.all():
                inmueble.delete()
        self.save()
 
    def __str__(self):
        if self.is_superuser:
            return self.username
        else:
            return self.nombres
    
    def save(self, *args, **kwargs):
        # Asigna un RUT único si el usuario es un superusuario y el RUT está vacío
        if self.is_superuser and not self.rut:
            self.tipo_usuario = 'administrador'  # Asignamos el tipo 'admin' para superusuarios
            self.rut = str(uuid.uuid4())[:9]  # Generamos un RUT único de 12 caracteres
        super().save(*args, **kwargs)



class Region(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.nombre
class Comuna(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='comunas')
    
    class Meta:
        ordering = ["nombre"]
    
    
    def __str__(self):
        return self.nombre


TIPO_INMUEBLES = [
    ('casa','Casa'),
    ('departamento','Departamento'),
    ('parcela','Parcela'),
]

class Inmueble(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    m2_construidos = models.FloatField()
    m2_totales = models.FloatField()
    estacionamientos = models.IntegerField()
    habitaciones = models.IntegerField()
    banos = models.IntegerField()
    direccion = models.CharField(max_length=200)
    #comuna = models.CharField(max_length=100)
    comuna = models.ForeignKey(Comuna,on_delete=models.CASCADE,null=True,blank=True)
    tipo_inmueble = models.CharField(max_length=50, choices=TIPO_INMUEBLES)
    precio_mensual = models.DecimalField(max_digits=10, decimal_places=2)
    dueño = models.ForeignKey(Usuario, on_delete=models.CASCADE,limit_choices_to={'tipo_usuario': 'arrendador'},related_name='inmuebles')
    is_active = models.BooleanField(default=True, editable=False)
    deleted_at = models.DateTimeField(blank=True,null=True, editable=False)
    
    # def delete(self, *args, **kwargs):
    #     self.is_active = False
    #     self.deleted_at = now()
    #     self.save()
    
    # def clean(self):
    #     if self.dueño and self.dueño.tipo_usuario != 'arrendador':
    #         raise ValidationError("El usuario seleccionado no es un arrendador.")
    
    def __str__(self):
        return self.nombre


class Foto(models.Model):
    descripcion = models.CharField(max_length=255, blank=True, null=True, default='')
    foto = models.ImageField(upload_to='inmuebles/')
    inmueble = models.ManyToManyField(Inmueble,related_name='fotos')