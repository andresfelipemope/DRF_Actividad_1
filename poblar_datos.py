from biblioteca.models import Autor, Libro, Resena
from datetime import date

#Autor.objects.create(nombre="", nacionalidad="")
autor1 = Autor.objects.create(nombre="Homero", nacionalidad="Grecia")
autor2 = Autor.objects.create(nombre="Dante Alighieri", nacionalidad="Italia")
autor3 = Autor.objects.create(nombre="John Green", nacionalidad="Estados Unidos")

# Libro.objects.create(
#     titulo = "",
#     autor = ,
#     fecha_publicacion = date(, ,),
#     resumen = ""
# )

libro1 = Libro.objects.create(
    titulo = "La Ilíada",
    autor = autor1,
    fecha_publicacion = date(800, 1, 1),
    resumen = "Relato épico de la guerra de Troya y el papel de Aquiles."
)

libro2 = Libro.objects.create(
    titulo = "La Odisea",
    autor = autor1,
    fecha_publicacion = date(750, 1, 1),
    resumen = "Viaje de Odiseo para volver a Ítaca tras la guerra."
)

libro3 = Libro.objects.create(
    titulo = "Himnos Homéricos",
    autor = autor1,
    fecha_publicacion = date(700, 1, 1),
    resumen = "Poemas dedicados a diferentes dioses del Olimpo."
)

libro4 =Libro.objects.create(
    titulo = "La Divina Comedia",
    autor = autor2,
    fecha_publicacion = date(1320, 1, 1),
    resumen = "Dante viaja por el Infierno, Purgatorio y Paraíso guiado por Virgilio."
)

libro5 = Libro.objects.create(
    titulo = "Vita Nuova",
    autor = autor2,
    fecha_publicacion = date(1295, 1, 1),
    resumen = "Colección de poemas sobre el amor platónico hacia Beatriz."
)

libro6 = Libro.objects.create(
    titulo = "De Monarchia",
    autor = autor2,
    fecha_publicacion = date(1313, 1, 1),
    resumen = "Tratado político sobre la relación entre Iglesia y Estado."
)

libro7 = Libro.objects.create(
    titulo = "Bajo la Misma Estrella",
    autor = autor3,
    fecha_publicacion = date(2012, 1, 10),
    resumen = "Historia de amor entre dos adolescentes que luchan contra el cáncer."
)

libro8 = Libro.objects.create(
    titulo = "Ciudades de Papel",
    autor = autor3,
    fecha_publicacion = date(2008, 10, 16),
    resumen = "Un joven busca a una chica misteriosa que desaparece repentinamente."
)

libro9 = Libro.objects.create(
    titulo = "El Teorema de Katherine",
    autor = autor3,
    fecha_publicacion = date(2006, 5, 30),
    resumen = "Un chico intenta demostrar por qué sus novias se llaman Katherine."
)

# Resena.objects.create(
#     libro = Libro.objects.get(titulo=""),
#     texto = "",
#     calificacion = 
# )

Resena.objects.create(
    libro = Libro.objects.get(titulo="La Ilíada"),
    texto = "Una obra épica impresionante y muy profunda.",
    calificacion = 5
)

Resena.objects.create(
    libro = Libro.objects.get(titulo="La Odisea"),
    texto = "Increíble aventura, pero un poco extensa.",
    calificacion = 4
)

Resena.objects.create(
    libro = Libro.objects.get(titulo="Himnos Homéricos"),
    texto = "Interesante pero menos conocido.",
    calificacion = 3
)

Resena.objects.create(
    libro = Libro.objects.get(titulo="La Divina Comedia"),
    texto = "Una obra maestra de la literatura universal.",
    calificacion = 5
)

Resena.objects.create(
    libro = Libro.objects.get(titulo="Vita Nuova"),
    texto = "Poético y romántico, aunque difícil de leer.",
    calificacion = 4
)

Resena.objects.create(
    libro = Libro.objects.get(titulo="De Monarchia"),
    texto = "Interesante perspectiva política.",
    calificacion = 3
)

Resena.objects.create(
    libro = Libro.objects.get(titulo="Bajo la Misma Estrella"),
    texto = "Emocionante, triste y muy humana.",
    calificacion = 5
)

Resena.objects.create(
    libro = Libro.objects.get(titulo="Ciudades de Papel"),
    texto = "Buen misterio pero final predecible.",
    calificacion = 3
)

Resena.objects.create(
    libro = Libro.objects.get(titulo="El Teorema de Katherine"),
    texto = "Divertido y original, aunque algo repetitivo.",
    calificacion = 4
)
