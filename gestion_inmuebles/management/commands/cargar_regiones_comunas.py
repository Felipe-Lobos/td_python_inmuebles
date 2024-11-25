import json
from django.core.management.base import BaseCommand
from gestion_inmuebles.models import Region, Comuna


class Command(BaseCommand):
    help = 'Carga regiones y comunas desde un archivo JSON'

    def handle(self, *args, **kwargs):
        # Cargar datos desde el archivo JSON
        with open('gestion_inmuebles/management/commands/regiones_comunas.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Iterar sobre las regiones y comunas
        for region_data in data['regiones']:
            region_nombre = region_data['region']
            
            # Crear o obtener la región
            region, created = Region.objects.get_or_create(nombre=region_nombre)
            self.stdout.write(self.style.SUCCESS(f"Región '{region_nombre}' cargada exitosamente"))
            
            # Crear las comunas asociadas
            for comuna_nombre in region_data['comunas']:
                Comuna.objects.get_or_create(nombre=comuna_nombre, region=region)
                self.stdout.write(self.style.SUCCESS(f"Comuna '{comuna_nombre}' cargada exitosamente"))

        self.stdout.write(self.style.SUCCESS('¡Datos cargados exitosamente!'))
