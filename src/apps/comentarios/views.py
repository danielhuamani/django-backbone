from django.shortcuts import render
from rest_framework import viewsets
from .models import Comentario
from .serializers import ComentarioSerializer
# Create your views here.


class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
