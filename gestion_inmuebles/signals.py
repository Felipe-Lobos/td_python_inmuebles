from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from gestion_inmuebles.models import Usuario

@receiver(post_save, sender=Usuario)
def asignar_grupo_por_defecto(sender, instance, created, **kwargs):
    if created:
         #asignar grupos
        match(instance.tipo_usuario):
            case 'administrador':
                grupo = Group.objects.get(name='administradores')
            case 'arrendador':
                grupo = Group.objects.get(name='arrendadores')
            case 'arrendatario':
                grupo = Group.objects.get(name='arrendatarios')
               
        # grupo = Group.objects.get(name="Gestores de Inmuebles")
        instance.groups.add(grupo)
        print(f"Usuario {instance.username} añadido al grupo '{grupo.name}' automáticamente")
