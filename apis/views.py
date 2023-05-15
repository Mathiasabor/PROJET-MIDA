from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from .models import Livre
from .models import Theses
from .models import Consultes
from .models import Categories
from .models import Telecharge

from rest_framework.viewsets import ModelViewSet
from rest_framework.viewsets import ReadOnlyModelViewSet
from django.contrib.auth import get_user_model
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import LivreSerializer
from .serializers import ThesesSerializer
from .serializers import ConsultesSerializer
from .serializers import CategoriesSerializer
from .serializers import TelechargeSerializer
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated

class LivreViewset(ModelViewSet):

    serializer_class = LivreSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Livre.objects.all()


class CategoriesViewset(ModelViewSet):

    serializer_class = CategoriesSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Categories.objects.all()


class ConsultesViewset(ModelViewSet):
    serializer_class = ConsultesSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Consultes.objects.all()

class ThesesViewset(ModelViewSet):
    serializer_class = ThesesSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Theses.objects.all()

class TelechargeViewset(ModelViewSet):
    serializer_class = TelechargeSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Telecharge.objects.all()

class UserViewset(ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return  get_user_model().objects.all()


class SingleUserViewset(ModelViewSet):
    serializer_class = UserSerializer
    #permission_classes = [IsAuthenticated]
    def get_queryset(self, pk =None):
        user = self.request.user
        queryset = User.objects.filter(pk=user.pk)
        return queryset
