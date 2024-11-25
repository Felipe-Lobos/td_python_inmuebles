import json
import os
import sys
import django


# # Asegúrate de que el directorio del proyecto esté en el path
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'proyecto_inmuebles')))
# # # Configurar el entorno Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto_inmuebles.settings')  # Ajusta el nombre según tu proyecto
django.setup()
# Importa tus modelos
from gestion_inmuebles.models import Region, Comuna

print('inicio script \n')
# Carga del archivo JSON
# with open('scripts/regiones_comunas.json', 'r', encoding='utf-8') as file:
#     data = json.load(file)

# # Iterar sobre las regiones y comunas
# for region_data in data['regiones']:
#     region_nombre = region_data['region']
#     region, region_created = Region.objects.get_or_create(nombre=region_nombre)
#     if region_created:
#         print(f"- {region_nombre} --- fue creada.")
#     else:
#         print(f"- {region_nombre} --- ya existia.")
#     for comuna_nombre in region_data['comunas']:
#         comuna, comuna_created =  Comuna.objects.get_or_create(nombre=comuna_nombre, region=region)
#         if comuna_created:
#             print(f"------ {comuna_nombre} ---- fue creada.")
#         else:
#             print(f"------ {comuna_nombre} ---- ya existia.")

# Fin de la ejecucion
print('Fin del script')

