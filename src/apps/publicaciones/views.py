from django.shortcuts import render
from rest_framework import viewsets
from .models import Noticia, TipoNoticia
from .serializers import NoticiaSerializer, TipoNoticiaSerializer


class NoticiaViewSet(viewsets.ModelViewSet):
    queryset = Noticia.objects.all()
    serializer_class = NoticiaSerializer


class TipoNoticiaViewSet(viewsets.ModelViewSet):
    queryset = TipoNoticia.objects.all()
    serializer_class = TipoNoticiaSerializer


def home(request):
    tipo_noticias = TipoNoticia.objects.all()
    return render(request, 'publicaciones.html', locals())
