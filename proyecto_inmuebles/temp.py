import os
import django
import pathlib
print(pathlib.Path().resolve())
print(pathlib.Path(__file__).parent.resolve())

# print(os.path)
# os.environ.setdefault("DJANGO_SETTINGS_MODULE","proyecto_inmuebles.settings")
# django.setup()

# from gestion_inmuebles.models import Usuario

# usuarios = Usuario.objects.all()
# print(usuarios)
