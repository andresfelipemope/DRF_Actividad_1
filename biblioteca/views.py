from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Avg
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

    def get_queryset(self):
        queryset = super().get_queryset()
        calificacion_min = self.request.query_params.get('calificacion_minima')

        if calificacion_min:
            queryset = queryset.filter(calificacion__gte=calificacion_min)
        return queryset
    
    @action(detail=False, methods=['get'])
    def promedio(self, request):
        libro_id = request.query_params.get('libro_id')

        if libro_id:
            promedio = Resena.objects.filter(libro__id=libro_id).aggregate(Avg('calificacion'))
            return Response({
                "libro_id": libro_id,
                "rating_promedio": promedio
            })
        
    def perform_create(self, serializer):
        serializer.save()