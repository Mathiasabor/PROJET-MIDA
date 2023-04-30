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
from apis.views import ThesesViewset
from apis.views import TelechargeViewset
from apis.views import UserViewset

from django.urls import re_path


router = routers.SimpleRouter()
router.register('categories',CategoriesViewset, basename ='categories')
router.register('livres',LivreViewset, basename ='categories')
router.register('consultes',ConsultesViewset, basename ='consultes')
router.register('theses',ThesesViewset, basename ='theses')
router.register('telecharges',TelechargeViewset, basename ='telecharges')
router.register('users',UserViewset, basename ='users')


urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path('apis/', include(router.urls)),
    re_path('api-auth/', include('rest_framework.urls')),
   re_path('apis/livres/rest-auth/', include('rest_auth.urls')),
   re_path('apis/livres/rest-auth/registration/', include('rest_auth.registration.urls')),

]
