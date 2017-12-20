
from rest_framework_mongoengine import serializers
from models import Publicacion
class PublicacionSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Publicacion
        fields = '__all__'