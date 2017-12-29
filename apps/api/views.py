# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Create your views here.
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from rest_framework_mongoengine import viewsets
<<<<<<< HEAD
from models import Publicacion
from models import User,CategoriaPost,Notificacion,Apoyo
from serializers import*
=======
from models import *
from serializers import *
>>>>>>> d2cc8b8325d9febe9a7250a94d4cffcbc481116f
import datetime


class PublicacionViewSet(viewsets.ModelViewSet):
   
    lookup_field = 'id'
    serializer_class = PublicacionSerializer

    def get_queryset(self):
        return Publicacion.objects.all()


class UserViewSet(viewsets.ModelViewSet):
 
    lookup_field = 'id'
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()

class PerfilViewSet(viewsets.ModelViewSet):
    
    lookup_field = 'id'
    serializer_class = PerfilSerializer

    def get_queryset(self):
        return Perfil.objects.all()

class NotificacionViewSet(viewsets.ModelViewSet):
 
    lookup_field = 'id'
    serializer_class = NotificacionSerializer

    def get_queryset(self):
        return Notificacion.objects.all()

class CategoriaViewSet(viewsets.ModelViewSet):

    lookup_field = 'id'
    serializers_class = CategoriaSerializer

    def get_queryset(self):
        return CategoriaPost.objets.all()