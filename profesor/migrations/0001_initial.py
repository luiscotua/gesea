# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-13 23:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('nombres', models.CharField(max_length=30)),
                ('id_ucc', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('estado', models.CharField(choices=[(b'ACTIVO', b'Activo'), (b'INACTIVO', b'Inactivo')], max_length=20)),
            ],
        ),
    ]
