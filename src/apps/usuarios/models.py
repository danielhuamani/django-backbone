# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.


class Usuario(models.Model):
    email = models.EmailField("Email")
    nombre = models.CharField("Nombres", max_length=100, blank=True)
    apellido = models.CharField("Apellidos", max_length=100, blank=True)
    password = models.CharField(u"Contraseña", max_length=100)

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __unicode__(self):
        return '%s - %s' % (self.email, self.nombre)
