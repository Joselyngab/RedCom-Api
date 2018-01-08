# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Create your views here.
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from rest_framework_mongoengine import viewsets
from rest_framework import permissions
from models import *
from serializers import *
import datetime




class PublicacionViewSet(viewsets.ModelViewSet):
   
  #  permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'id'
    serializer_class = PublicacionSerializer

    def get_queryset(self):
        return Publicacion.objects.all()


class UserViewSet(viewsets.ModelViewSet):
 
    lookup_field ='id'
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()

<<<<<<< HEAD
class PerfilViewSet(viewsets.ModelViewSet):
    
   # permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'id'
    serializer_class = PerfilSerializer
=======
>>>>>>> b1104a731f1ecd838ed84ff68cae5b99db73feca


class NotificacionViewSet(viewsets.ModelViewSet):
 
    lookup_field = 'id'
    serializer_class = NotificacionSerializer

    def get_queryset(self):
        return Notificacion.objects.all()

class CategoriaPostViewSet(viewsets.ModelViewSet):

    lookup_field = 'nombre'
    serializer_class = CategoriaPostSerializer

    def get_queryset(self):
        return CategoriaPost.objects.all()

class EstadoViewSet(viewsets.ModelViewSet):

    lookup_field = 'id'
    serializer_class = EstadoSerializer

    def get_queryset(self):
        return Estado.objects.all()
