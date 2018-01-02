
from rest_framework_mongoengine import serializers
from models import *


class PublicacionSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Publicacion
        fields = '__all__'

class UserSerializer(serializers.DocumentSerializer):
    class Meta:
        model = User
        fields = '__all__'

class PerfilSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Perfil
        fields ='__all__'

class NotificacionSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Notificacion
        fields = '__all__'
        exclude = ('visto = 1')
        
class CategoriaPostSerializer(serializers.DocumentSerializer):
    class Meta:
        model = CategoriaPost
        fields = '__all__'