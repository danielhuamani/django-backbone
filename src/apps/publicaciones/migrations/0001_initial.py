# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=120, verbose_name=b'Titulo')),
                ('descripcion', models.TextField(verbose_name=b'descripcion')),
                ('fecha', models.DateTimeField(auto_now_add=True, verbose_name=b'Fecha')),
            ],
            options={
                'verbose_name': 'Noticia',
                'verbose_name_plural': 'Noticias',
            },
        ),
    ]
