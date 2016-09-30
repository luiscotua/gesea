# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('Nombre', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=30)),
                ('id_ucc', models.PositiveSmallIntegerField(serialize=False, primary_key=True)),
                ('Identificacion', models.PositiveSmallIntegerField()),
                ('estado', models.CharField(max_length=20, choices=[(b'ACTIVO', b'Activo'), (b'INACTIVO', b'Inactivo')])),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
