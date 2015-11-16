# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publicaciones', '0002_noticia_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoNoticia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(max_length=120, verbose_name=b'Tipo de noticia')),
            ],
            options={
                'verbose_name': 'TipoNoticia',
                'verbose_name_plural': 'TipoNoticias',
            },
        ),
        migrations.AddField(
            model_name='noticia',
            name='tipo',
            field=models.ForeignKey(related_name='tipo_noticia', to='publicaciones.TipoNoticia', null=True),
        ),
    ]
