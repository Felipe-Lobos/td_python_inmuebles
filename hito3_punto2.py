# asdas

import os
import django
# Ajusta el nombre según tu proyecto
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto_inmuebles.settings')
django.setup()

from gestion_inmuebles.models import Inmueble, Comuna
print('inicio srcript')
id_comunas_con_inmuebles=[]
inmuebles_comunas = Inmueble.objects.raw('SELECT id, comuna_id FROM gestion_inmuebles_inmueble GROUP BY comuna_id')
for com_id in inmuebles_comunas:
    id_comunas_con_inmuebles.append(com_id.comuna_id)

lista_comuna_inmueble = []
for id_comuna in id_comunas_con_inmuebles:
    comuna = Comuna.objects.get(id=id_comuna)
    inmuebles=Inmueble.objects.filter(comuna=comuna).all()
    lista_comuna_inmueble.append({'comuna':comuna,'inmueble': inmuebles})

with open('hito3_2.txt', 'w+',encoding="utf-8") as file:
    for c in lista_comuna_inmueble:
        file.write(str(c['comuna']))
        file.write(',\n')
        for i in c['inmueble']:
            file.write(str('----'+i.nombre))
            file.write(',\n')
            #file.write(str('---- -----'+i.descripcion))
print('fin srcript')
