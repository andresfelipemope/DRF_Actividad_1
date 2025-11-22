from rest_framework import serializers
from .models import Autor, Libro, Resena

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'

class ResenaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resena
        fields = '__all__'

class LibroSerializer(serializers.ModelSerializer):
    autor_name = serializers.ReadOnlyField(source="autor.nombre")
    recent_views = serializers.SerializerMethodField()

    class Meta:
        model = Libro
        fields = ('titulo', 'autor_name', 'fecha_publicacion', 'resumen', 'recent_views')

    def get_recent_views(self, obj) :
        reviews = obj.resenas.order_by('-fecha')[:2]
        return ResenaSerializer(reviews, many=True).data