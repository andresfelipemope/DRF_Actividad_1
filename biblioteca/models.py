from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator

def validate_autor(autor):
    if autor.strip() == "" :
        raise ValidationError("El nombre del autor es invalido")
    
def validate_libro(libro):
    if libro.strip()=="" or len(libro) < 10:
        raise ValidationError("El resumen no cuenta con la cantidad minima de 10 caracteres")

def validate_resena(resena):
    if resena < 0 or resena > 5:
        raise ValidationError("La calificacion debe estar en un rango entre 0 y 5")

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(
        max_length=100,
        validators=[validate_autor]
        )
    nacionalidad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='libros')
    fecha_publicacion = models.DateField(null=True, blank=True)
    resumen = models.TextField(
        validators=[validate_libro]
    )

    def __str__(self):
        return self.titulo
    
class Resena(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='resenas')
    texto = models.TextField()
    calificacion = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5)
        ]
    )
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.libro.titulo} - {self.calificacion}/5"