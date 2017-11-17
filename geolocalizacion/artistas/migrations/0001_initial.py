# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-10 23:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_google_maps.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido_p', models.CharField(max_length=30)),
                ('apellido_m', models.CharField(max_length=30)),
                ('sexo', models.CharField(max_length=20)),
                ('correo', models.CharField(max_length=50)),
                ('nombre_artis', models.CharField(max_length=30)),
                ('curriculum', models.CharField(max_length=500)),
                ('nombre_com', models.CharField(max_length=30)),
                ('cargo', models.CharField(max_length=30)),
                ('semblanza', models.CharField(max_length=500)),
                ('dir_usu', models.CharField(max_length=50)),
                ('dir_com', models.CharField(max_length=50)),
                ('foto_per', models.CharField(max_length=400)),
                ('foto_com', models.CharField(max_length=400)),
                ('red_soc_per', models.CharField(max_length=400)),
                ('red_soc_com', models.CharField(max_length=400)),
                ('web', models.CharField(max_length=400)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Coleccionista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido_p', models.CharField(max_length=30)),
                ('apellido_m', models.CharField(max_length=30)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pieza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=30)),
                ('tecnica', models.CharField(max_length=30)),
                ('tipo_prod', models.CharField(max_length=30)),
                ('disciplina', models.CharField(max_length=30)),
                ('sinopsis', models.CharField(max_length=500)),
                ('ano_creac', models.IntegerField()),
                ('num_pers_prod', models.IntegerField()),
                ('num_pers_tal', models.IntegerField()),
                ('tipo_foro', models.CharField(max_length=30)),
                ('aforo_obra', models.CharField(max_length=30)),
                ('tipo_financ', models.CharField(max_length=30)),
                ('foto_cartel', models.CharField(max_length=400)),
                ('url_video', models.CharField(max_length=400)),
                ('observaciones', models.CharField(max_length=400)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('artista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artistas.Artista')),
                ('coleccionista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artistas.Coleccionista')),
            ],
        ),
        migrations.CreateModel(
            name='Programador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido_p', models.CharField(max_length=30)),
                ('apellido_m', models.CharField(max_length=30)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('financiamiento', models.CharField(max_length=30)),
                ('ano_present', models.IntegerField()),
                ('tipo_gestion', models.CharField(max_length=30)),
                ('num_presen', models.IntegerField()),
                ('pieza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artistas.Pieza')),
                ('programador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artistas.Programador')),
            ],
        ),
        migrations.CreateModel(
            name='Sede',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_sede', models.CharField(max_length=30)),
                ('tipo_sede', models.CharField(max_length=30)),
                ('address', django_google_maps.fields.AddressField(max_length=200)),
                ('geolocation', django_google_maps.fields.GeoLocationField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='registro',
            name='sede',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artistas.Sede'),
        ),
    ]
