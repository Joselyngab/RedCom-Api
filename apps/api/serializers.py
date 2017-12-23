
from rest_framework_mongoengine import serializers
from models import Publicacion
from models import User
from models import CategoriaPost,Notificacion, Apoyo
class PublicacionSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Publicacion
        fields = '__all__'

class UserSerializer(serializers.DocumentSerializer):
    class Meta:
        model = User
        dept = 2
        fields = '__all__'

class CategoriaPostSerializer(serializers.DocumentSerializer):
     class Meta:
        model = CategoriaPost
        fields = '__all__'

class NotificacionSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Notificacion
        fields = '__all__'

class ApoyoSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Apoyo
        fields = '__all__'