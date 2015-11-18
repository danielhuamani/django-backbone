from django.db import models


# Create your models here.
class TipoNoticia(models.Model):

    tipo = models.CharField("Tipo de noticia", max_length=120)

    class Meta:
        verbose_name = "TipoNoticia"
        verbose_name_plural = "TipoNoticias"

    def __unicode__(self):
        return self.tipo


class Noticia(models.Model):
    tipo = models.ForeignKey(TipoNoticia, related_name='tipo_noticia', null=True)
    titulo = models.CharField("Titulo", max_length=120)
    descripcion = models.TextField("descripcion")
    imagen = models.ImageField("Imagen", upload_to="noticia", blank=True)
    fecha = models.DateTimeField("Fecha", auto_now_add=True)

    class Meta:
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"

    def __str__(self):
        return self.titulo
