# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publicaciones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='imagen',
            field=models.ImageField(default='', upload_to=b'noticia', verbose_name=b'Imagen'),
            preserve_default=False,
        ),
    ]
