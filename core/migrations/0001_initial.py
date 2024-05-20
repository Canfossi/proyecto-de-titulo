# Generated by Django 3.1.3 on 2024-04-29 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('codigo', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('creditos', models.PositiveSmallIntegerField()),
                ('servicio', models.CharField(max_length=50)),
                ('fecha_hora', models.DateTimeField()),
                
            ],
        ),
    ]
