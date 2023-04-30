from django.urls import path
from .views import LivreViewset
from .views import CategoriesViewset
from .views import ConsultesViewset
from .views import ThesesViewset
from .views import TelechargeViewset



# Ici nous créons notre routeur


urlpatterns =[

   # path('Livres',LivreAPIView.as_view()),
   # path('',CategoriesAPIView.as_view()),
   # path('Consultes', ConsultesAPIView.as_view()),
   # path('Theses', ThesesAPIView.as_view()),
   # path('Telecharges', TelechargeAPIView.as_view()),
]