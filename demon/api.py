from rest_framework import viewsets

from .models import Personaje, Arma, UsuarioPersonalizado

from .serializers import ArmaSerializer, PJSerializer, UserSerializer

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

class ArmaViewSet(viewsets.ModelViewSet):
    queryset = Arma.objects.all()
    serializer_class = ArmaSerializer

class PersonajeViewSet(viewsets.ModelViewSet):
    queryset = Personaje.objects.all()
    serializer_class = PJSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset= UsuarioPersonalizado.objects.all()
    serializer_class = UserSerializer
