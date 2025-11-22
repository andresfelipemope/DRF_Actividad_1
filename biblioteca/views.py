from django.shortcuts import render
from rest_framework import viewsets
from .models import Autor, Libro, Resena
from .serializers import AutorSerializer, LibroSerializer, ResenaSerializer

# Create your views here.
class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    filterset_fields = ['nacionalidad']
    search_fields = ['nombre', 'nacionalidad']
    ordering_fields = ['nombre']

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all().select_related('autor')
    serializer_class = LibroSerializer
    filterset_fields = ['autor__nombre', 'autor__id', 'fecha_publicacion']
    search_fields = ['titulo', 'autor__nombre', 'autor__id']
    ordering_fields = ['titulo', 'fecha_publicacion']

class ResenaViewSet(viewsets.ModelViewSet):
    queryset = Resena.objects.all().select_related('libro')
    serializer_class = ResenaSerializer
    filterset_fields = ['libro__titulo', 'libro__id', 'calificacion']
    search_fields = ['libro__titulo', 'libro__id', 'fecha', 'calificacion']
    ordering_fields = ['fecha', 'calificacion']