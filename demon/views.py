from django.shortcuts import render
from django.http import HttpResponse

from demon.models import Personaje
from .serializers import PJSerializer, ArmaSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


@require_http_methods(["GET"])
class ListUsers(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        usernames = [ user.username for user in User.objects.all()]
        return Response(usernames)

@csrf_exempt
class PersonajesAPIView(APIView):
    #permission_classes = [IsAuthenticated]

    def get(self, request):
        personajes = Personaje.objects.filter(usuario=request.user).select_related("usuario")
        lista_pjs = []

        for pj in personajes:
            info_pj_ind = {
                "nombre": pj.nombre,
                "estado": pj.estado,
                "fecha_creacion": pj.fecha_creacion,
            }
            lista_pjs.append(info_pj_ind)

        return Response(lista_pjs)