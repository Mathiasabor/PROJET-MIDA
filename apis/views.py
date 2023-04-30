from django.shortcuts import render
from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Livre
from .models import Theses
from .models import Consultes
from .models import Categories
from .models import Telecharge

from rest_framework.viewsets import ModelViewSet
from rest_framework.viewsets import ReadOnlyModelViewSet


# Create your views here.

from .serializers import LivreSerializer
from .serializers import ThesesSerializer
from .serializers import ConsultesSerializer
from .serializers import CategoriesSerializer
from .serializers import TelechargeSerializer
from .serializers import UserSerializer

class LivreViewset(ModelViewSet):

    serializer_class = LivreSerializer
    def get_queryset(self):
        return Livre.objects.all()


class CategoriesViewset(ModelViewSet):

    serializer_class = CategoriesSerializer
    def get_queryset(self):
        return Categories.objects.all()


class ConsultesViewset(ModelViewSet):
    serializer_class = ConsultesSerializer
    def get_queryset(self):
        return Consultes.objects.all()

class ThesesViewset(ModelViewSet):
    serializer_class = ThesesSerializer
    def get_queryset(self):
        return Theses.objects.all()

class TelechargeViewset(ModelViewSet):
    serializer_class = TelechargeSerializer
    def get_queryset(self):
        return Telecharge.objects.all()

class UserViewset(ModelViewSet):
    serializer_class = UserSerializer
    def get_queryset(self):
        return  get_user_model().objects.all()

