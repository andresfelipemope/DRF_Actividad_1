from rest_framework import routers
from .views import AutorViewSet, LibroViewSet, ResenaViewSet

router = routers.DefaultRouter()
router.register(r'autores', AutorViewSet)
router.register(r'libros', LibroViewSet)
router.register(r'resenas', ResenaViewSet)

urlpatterns = router.urls