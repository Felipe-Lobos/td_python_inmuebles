# Generated by Django 5.1.3 on 2024-11-26 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_inmuebles', '0011_rename_inmuebles_foto_inmueble'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foto',
            name='foto',
            field=models.ImageField(upload_to='fotos/inmuebles/'),
        ),
    ]
