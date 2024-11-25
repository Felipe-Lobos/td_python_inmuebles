# Generated by Django 5.1.3 on 2024-11-15 15:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_inmuebles', '0004_inmueble_deleted_at_inmueble_is_active_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comunas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comunas', to='gestion_inmuebles.region')),
            ],
        ),
    ]
