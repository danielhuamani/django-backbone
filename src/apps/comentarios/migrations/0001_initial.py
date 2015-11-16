# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publicaciones', '0002_noticia_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField(auto_now_add=True, verbose_name=b'Fecha')),
                ('autor', models.CharField(max_length=120, verbose_name=b'Autor')),
                ('comentario', models.TextField(verbose_name=b'Comentario')),
                ('noticia', models.ForeignKey(related_name='noticia_comentario', to='publicaciones.Noticia')),
            ],
            options={
                'verbose_name': 'Comentario',
                'verbose_name_plural': 'Comentarios',
            },
        ),
    ]
