# Generated by Django 5.1.3 on 2024-11-26 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_inmuebles', '0012_alter_foto_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foto',
            name='foto',
            field=models.ImageField(upload_to='inmuebles/'),
        ),
    ]
