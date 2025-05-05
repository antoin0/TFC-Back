from django.urls import path
from rest_framework import routers
from .api import ArmaViewSet, PersonajeViewSet, UserViewSet
from rest_framework.authtoken.views import ObtainAuthToken

router = routers.DefaultRouter()

router.register('api/armas', ArmaViewSet,'armas')

router.register('api/pejotas', PersonajeViewSet,'pejotas')

router.register('api/users', UserViewSet,'usuario')

urlpatterns = router.urls



