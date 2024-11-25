# asdas

import os
import django
from django.db import connection

# Ajusta el nombre según tu proyecto
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto_inmuebles.settings')
django.setup()

from gestion_inmuebles.models import Inmueble, Comuna
print('inicio srcript')
inmuebles = Inmueble.objects.all()
sql_raw='SELECT gii.id,gic.region_id from gestion_inmuebles_inmueble gii inner join gestion_inmuebles_comuna gic on gic.id = gii.comuna_id group by gic.region_id'
regiones_inmueble = Inmueble.objects.raw(sql_raw)
with open('hito3_3.txt', 'w+',encoding="utf-8") as file:
    for ri in regiones_inmueble:
        file.write(str(f'> {ri.comuna.region.nombre}'))
        file.write(',\n')
        inmueble_ri = Inmueble.objects.filter(comuna__region_id=ri.region_id)
        for inmueble in inmueble_ri:
            file.write(str(f'------ {inmueble.nombre}'))
            file.write(',\n')
            #file.write(str('---- -----'+i.descripcion))
print('fin srcript')