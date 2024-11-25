import json
from gestion_inmuebles.models import Region, Comuna

##EJECUTAR CON:
# python manage.py shell < print_regiones_comunas.py

print('inicio script \n')
# Carga del archivo JSON
with open('scripts/regiones_comunas.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Iterar sobre las regiones y comunas
for region_data in data['regiones']:
    region_nombre = region_data['region']
    region, region_created = Region.objects.get_or_create(nombre=region_nombre)
    if region_created:
        print(f"- {region_nombre} --- fue creada.")
    else:
        print(f"- {region_nombre} --- ya existia.")
    for comuna_nombre in region_data['comunas']:
        comuna, comuna_created =  Comuna.objects.get_or_create(nombre=comuna_nombre, region=region)
        if comuna_created:
            print(f"------ {comuna_nombre} ---- fue creada.")
        else:
            print(f"------ {comuna_nombre} ---- ya existia.")

# Fin de la ejecucion
print('Fin del script')
