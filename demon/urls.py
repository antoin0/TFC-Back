from django.urls import path
from rest_framework import routers
from .api import ArmaViewSet, PersonajeViewSet, UserViewSet
from rest_framework.authtoken.views import ObtainAuthToken
from .models import Arma, Personaje
from .views import ListUsers, PersonajesAPIView
router = routers.DefaultRouter()

router.register('api/armas', ArmaViewSet,'armas')

router.register('api/pejotas', PersonajeViewSet,'pejotas')

router.register('api/users', UserViewSet,'usuario')



urlpatterns = router.urls

urlpatterns = [
    path('api-token-auth/', ObtainAuthToken.as_view(), name='api_token_auth'),
    path('personajes/', PersonajesAPIView.as_view(),name = 'personajes_usuario'),
]



