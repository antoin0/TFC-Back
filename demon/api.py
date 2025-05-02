from rest_framework import viewsets

from .models import Personaje, Arma, UsuarioPersonalizado

from .serializers import ArmaSerializer, PJSerializer

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

class ArmaViewSet(viewsets.ModelViewSet):
    queryset = Arma.objects.all()
    serializer_class = ArmaSerializer

class PersonajeViewSet(viewsets.ModelViewSet):
    queryset = Personaje.objects.all()
    serializer_class = PJSerializer


    @action(detail=True,methods=['post'])
    def unalive(self, request, pk= None):
        pejota = self.get_object()
        pejota.estado = not pejota.estado
        pejota.save()
        return Response({
            'status': 'morto' if pejota.estado=="muerto" else 'vivo!'
        }, status = status.HTTP_200_OK)



class UserViewSet(viewsets.ModelViewSet):
    queryset= UsuarioPersonalizado.objects.all()
