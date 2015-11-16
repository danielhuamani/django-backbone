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
    return render(request, 'noticias.html', locals())

