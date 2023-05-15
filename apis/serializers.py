from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Livre
from .models import Theses
from .models import Consultes
from .models import Categories
from .models import Telecharge


class UserSerializer(ModelSerializer): # new
        class Meta:
            model = get_user_model()
            fields = ('id','email', 'username','password','first_name','last_name','is_active')

class CategoriesSerializer(ModelSerializer):

    class Meta:
        model = Categories
        fields =['nom','id']


class LivreSerializer(ModelSerializer):
    ccategoried = CategoriesSerializer()
    class Meta:
        model = Livre
        fields=['id','isbn','description','linodate','editions','exemplaire','categoried']



class ConsultesSerializer(ModelSerializer):
    class Meta:
        model = Consultes
        fields=['date','livred']

class ThesesSerializer(ModelSerializer):
    class Meta:
        model = Theses
        fields =['id','name','link']

class TelechargeSerializer(ModelSerializer):
    class Meta:
        model =Telecharge
        fields =['dates','thesed']