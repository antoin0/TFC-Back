from django.shortcuts import render
from django.http import HttpResponse
from .serializers import PJSerializer, ArmaSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse


@require_http_methods(["GET"])
class ListUsers(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        usernames = [ user.username for user in User.objects.all()]
        return Response(usernames)



@require_http_methods(["POST"])
class crearPejota(APIView):
    authentication_classes = [permissions.IsAuthenticated]

    def post(self, request):
        return Response({"mensaje":"q pàsa tarantula"})