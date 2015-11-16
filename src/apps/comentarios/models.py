from django.db import models
from apps.publicaciones.models import Noticia
# Create your models here.


class Comentario(models.Model):
    noticia = models.ForeignKey(Noticia, related_name='noticia_comentario')
    fecha = models.DateTimeField("Fecha", auto_now_add=True)
    autor = models.CharField("Autor", max_length=120)
    comentario = models.TextField("Comentario")

    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"

    def __unicode__(self):
        return u'%s - %s' % (self.autor, self.noticia)
