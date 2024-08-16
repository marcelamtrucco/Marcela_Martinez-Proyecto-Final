# Generated by Django 5.0.6 on 2024-08-11 01:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_rename_clases_clase_rename_entrenadores_entrenador_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='socio',
            name='id_socio',
            field=models.PositiveIntegerField(default='12345'),
        ),
        migrations.AlterField(
            model_name='socio',
            name='email',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='socio',
            name='telefono',
            field=models.CharField(max_length=50),
        ),
        migrations.CreateModel(
            name='Reserva_Clase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turno', models.CharField(choices=[('YOGA', 'Yoga_Lunes_ 10:00AM - 11:30AM'), ('YOGA', 'Yoga_Martes_ 2:00PM - 3:30PM'), ('PILATES', 'Pilates_Jueves_ 2:00PM - 3:30PM'), ('PILATES', 'Pilates_Viernes_ 10:00AM - 11:30AM'), ('ZUMBA', 'Zumba_Lunes_ 2:00PM - 3:30PM'), ('ZUMBA', 'Zumba_Martes_ 10:00AM - 11:30AM'), ('SPINNING', 'Spinning_Miércoles_ 10:00AM - 11:30AM'), ('SPINNING', 'Spinning_Viernes_ 2:00PM - 3:30PM'), ('MUSCULACIÓN', 'Musculación_Miércoles_ 10:00AM - 11:30AM'), ('MUSCULACIÓN', 'Musculación_Jueves_ 2:00PM - 3:30PM')], default='----', max_length=50)),
                ('clase', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='website.clase')),
                ('id_socio', models.ForeignKey(default='12345', on_delete=django.db.models.deletion.CASCADE, to='website.socio')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
