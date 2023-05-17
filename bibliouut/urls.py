"""
URL configuration for bibliouut project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from rest_framework import routers

from apis.views import LivreViewset
from apis.views import CategoriesViewset
from apis.views import ConsultesViewset
from apis.views import ConsultedViewset
from apis.views import ThesesViewset
from apis.views import TelechargeViewset
from apis.views import UserViewset
from apis.views import SingleUserViewset
from apis.views import TelechargedViewset

from django.urls import re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.SimpleRouter()
router.register('categories',CategoriesViewset, basename ='categories')
router.register('livres',LivreViewset, basename ='categories')
router.register('consultes',ConsultesViewset, basename ='consultes')
router.register(r'consulted',ConsultedViewset, basename='consultes-utilisateur')
router.register('theses',ThesesViewset, basename ='theses')
router.register('telecharges',TelechargeViewset, basename ='telecharges')
router.register(r'telecharged',TelechargedViewset, basename ='telecharges-utilisateur')
router.register('users',UserViewset, basename ='users')
router.register('singleuser',SingleUserViewset, basename='singleuser')

urlpatterns = [
    re_path('admin/', admin.site.urls),
     re_path('apis/', include(router.urls)),
     path('api-auth/', include('rest_framework.urls')),
    path('apis/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('apis/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
