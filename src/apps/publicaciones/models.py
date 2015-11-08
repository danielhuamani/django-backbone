from django.db import models


# Create your models here.
class Noticia(models.Model):
    titulo = models.CharField("Titulo", max_length=120)
    descripcion = models.TextField("descripcion")
    imagen = models.ImageField("Imagen", upload_to="noticia")
    fecha = models.DateTimeField("Fecha", auto_now_add=True)

    class Meta:
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"

    def __str__(self):
        return self.titulo
