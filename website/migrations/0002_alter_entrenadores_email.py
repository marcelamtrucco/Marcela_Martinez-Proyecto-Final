# Generated by Django 5.0.6 on 2024-07-22 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrenadores',
            name='email',
            field=models.EmailField(max_length=30),
        ),
    ]
