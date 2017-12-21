
from rest_framework_mongoengine import serializers
from models import Publicacion
from models import User
class PublicacionSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Publicacion
        fields = '__all__'

class UserSerializer(serializers.DocumentSerializer):
    class Meta:
        model = User
        dept = 2
        fields = '__all__'
        