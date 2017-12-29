# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Create your views here.
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from rest_framework_mongoengine import viewsets
from models import Publicacion
from models import User,CategoriaPost,Notificacion,Apoyo
from serializers import*
import datetime
class PublicacionViewSet(viewsets.ModelViewSet):
    '''
    Contains information about inputs/outputs of a single program
    that may be used in Universe workflows.
    '''
    lookup_field = 'id'
    serializer_class = PublicacionSerializer

    def get_queryset(self):
        return Publicacion.objects.all()
#Se define index donde recibe como argumento request
def index(request):
    #SI el metodo es un post, se toma los datos del formulario y se guarda en 
    #mongodb
    context_instance = ""
    if request.method == 'POST':
       # nuevo post
       title = request.POST['titulo']
       content = request.POST['contenido']

       publicacion = Publicacion(titulo=title)
       publicacion.fecha_update = datetime.datetime.now()
       publicacion.contenido = content
       publicacion.save()
   #Si el metodo es get entonces se está cargando la página inicialmente, así que se publican 
   #los posts
    # se obtiene todos los posts de la base de datos
    publicacion= Publicacion.objects
    context_instance=RequestContext(request)
    return render_to_response('indexPost.html', {'Publiacacions': publicacion},context_instance)


#Actualizar un post
def update(request):
    #Captura el id del post
    id = eval("request." + request.method + "['id']")
    post = Publicacion.objects(id=id)[0]
    #Si el metodo es post, se está actualizando la información del formulario
    if request.method == 'POST':
       
        # se actualiza los valores y se salva en mongodb
        post.titulo = request.POST['title']
        post.fecha_update = datetime.datetime.now()
        post.contenido = request.POST['content']
        post.save()
        template = 'indexPost.html'
        params = {'Posts': Publicacion.objects}
    #Si el metodo es GET se muestra la página incial update.html
    elif request.method == 'GET':
        template = 'updatePost.html'
        params = {'post':post}

    return render_to_response(template, params, context_instance=RequestContext(request))

#Para borrar un posts
def delete(request):
    #Se toma el id del post
    id = eval("request." + request.method + "['id']")
    #Se pregunta si es POST, se le pasa el id del posts y se borra, se va a la página index.html
    if request.method == 'POST':
        post = Publicacion.objects(id=id)[0]
        post.delete()
        template = 'indexPost.html'
        params = {'Posts': Publicacion.objects}
    #Si es un metodo get entonces se muestra la página delete.html
    elif request.method == 'GET':
        template = 'deletePost.html'
        params = { 'id': id }

    return render_to_response(template, params, context_instance=RequestContext(request))
class UserViewSet(viewsets.ModelViewSet):
    '''
    Contains information about inputs/outputs of a single program
    that may be used in Universe workflows.
    '''
    lookup_field = 'id'
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()

class CategoriaPostViewSet(viewsets.ModelViewSet):
    '''
    Contains information about inputs/outputs of a single program
    that may be used in Universe workflows.
    '''
    lookup_field = 'id'
    serializer_class = CategoriaPostSerializer

    def get_queryset(self):
        return CategoriaPost.objects.all()


class NotificacionViewSet(viewsets.ModelViewSet):
    '''
    Contains information about inputs/outputs of a single program
    that may be used in Universe workflows.
    '''
    lookup_field = 'id'
    serializer_class = NotificacionSerializer

    def get_queryset(self):
        return Notificacion.objects.all()

class ApoyoViewSet(viewsets.ModelViewSet):
    '''
    Contains information about inputs/outputs of a single program
    that may be used in Universe workflows.
    '''
    lookup_field = 'id'
    serializer_class = ApoyoSerializer

    def get_queryset(self):
        return Apoyo.objects.all()