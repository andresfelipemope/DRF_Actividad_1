# Biblioteca API (Django REST Framework)

API para gestionar una biblioteca con autores, libros y reseñas. Permite:
- Registrar autores.
- Agregar libros relacionados a un autor.
- Escribir reseñas con calificaciones.

Requisitos
- Python 3.8+
- pip
- virtualenv
- Dependencias: Django, djangorestframework

Instalación (Linux / macOS)
1. Sitúate en el proyecto:
   ```bash
   cd "@/Act1"
   ```

2. Crear y activar entorno virtual:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Instalar dependencias:
   - Si existe `requirements.txt`:
     ```bash
     pip install -r requirements.txt
     ```
   - Si no:
     ```bash
     pip install "Django>=4.2,<5" djangorestframework django-filter
     ```

4. Aplicar migraciones:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. (Opcional) Poblar la base de datos con datos de ejemplo:
   ```bash
   python3 manage.py shell < poblar_datos.py
   ```

6. Crear superusuario (para /admin):
   ```bash
   python manage.py createsuperuser
   ```

7. Ejecutar servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```

Uso
- Panel de administración: http://127.0.0.1:8000/admin/
- Endpoints API (ejemplo): http://127.0.0.1:8000/api/  
  (Las rutas exactas dependen de `biblioteca_project/urls.py`.)

Ejemplos de consultas (filtrado, búsqueda, orden)
- /api/books/?autor=1
- /api/books/?search=Soledad
- /api/books/?ordering=-fecha_publicacion

Notas importantes
- Las migraciones crean tablas en la BD, no registran modelos en el admin. Para ver modelos en /admin debes registrar cada modelo en `biblioteca/admin.py`.
- La DB por defecto es SQLite (`db.sqlite3`). Para reiniciar elimínala y vuelve a migrar.

Problemas comunes
- Si /admin no muestra modelos:
  - Verifica `biblioteca` en `INSTALLED_APPS` (archivo `biblioteca_project/settings.py`).
  - Asegúrate de haber registrado modelos en `biblioteca/admin.py`.
  - Crea un superusuario y reinicia el servidor.
