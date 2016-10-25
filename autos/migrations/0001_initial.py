# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-25 01:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Automovil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=30)),
                ('linea', models.CharField(max_length=30)),
                ('modelo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='automovil',
            name='marca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autos.Marca'),
        ),
    ]
