from rest_framework import serializers
from .models import Noticia, TipoNoticia
from apps.comentarios.models import Comentario


class TipoNoticiaSerializer(serializers.HyperlinkedModelSerializer):
    tipo_noticia = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='publicaciones:noticia-detail')

    class Meta:
        model = TipoNoticia
        fields = ('tipo_noticia', 'tipo')


class NoticiaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Noticia
        fields = ('titulo', 'descripcion', 'imagen', 'fecha', 'tipo')
