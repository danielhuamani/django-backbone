# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=254, verbose_name=b'Email')),
                ('nombre', models.CharField(max_length=100, verbose_name=b'Nombres', blank=True)),
                ('apellido', models.CharField(max_length=100, verbose_name=b'Apellidos', blank=True)),
                ('password', models.CharField(max_length=100, verbose_name='Contrase\xf1a')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
            },
        ),
    ]
