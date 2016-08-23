# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-15 13:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ReservaVuelos', '0004_vuelo'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegCompra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='RegUsuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=100)),
                ('Apellido', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
                ('password2', models.CharField(max_length=20)),
            ],
        ),
        migrations.RenameField(
            model_name='vuelo',
            old_name='ninio',
            new_name='niño',
        ),
        migrations.AddField(
            model_name='regcompra',
            name='idU',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ReservaVuelos.RegUsuario'),
        ),
        migrations.AddField(
            model_name='regcompra',
            name='idV',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ReservaVuelos.Vuelo'),
        ),
    ]