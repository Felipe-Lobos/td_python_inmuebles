# Generated by Django 5.1.3 on 2024-11-15 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_inmuebles', '0007_alter_inmueble_comuna'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inmueble',
            name='comuna',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]