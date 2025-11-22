from django.contrib import admin
from .models import Autor, Libro, Resena

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nacionalidad', 'cantidad_libros')
    search_fields = ('nombre', 'nacionalidad')
    ordering = ('nombre', 'nombre')

    def cantidad_libros(self, obj):
        return obj.libros.count()

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor')
    search_fields = ('titulo', 'autor__nombre')

@admin.register(Resena)
class ResenaAdmin(admin.ModelAdmin):
    list_display = ('libro', 'calificacion')
    search_fields = ('libro__titulo',)