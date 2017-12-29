# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from mongoengine import *
import  datetime

class CategoriaPost(Document):
    nombre = StringField(max_length=50,required=True, unique=True)
    fecha_create = DateTimeField(default = datetime.datetime.now)
    activa = BooleanField(default=True)

class User(Document):
    email= EmailField(unique=True)
    name = StringField(max_length=120)
    password= StringField(max_length=10)
    estado = StringField(default="")
    ciudad = StringField(default="")
    direccion = StringField(default="")
    seguidores = ListField(ReferenceField('self'))
    seguidos = ListField(ReferenceField('self'))
    notificaciones = ListField(ReferenceField('self'))
    modificado = DateTimeField(default = datetime.datetime.now)
    activo = BooleanField(default=True)
    meta = {'allow_inheritance': True}

class Ente(User):
    telefono = IntField(default=0, max_length=11)
    area_dedicada = ReferenceField(CategoriaPost)

class Persona(User):
    apellido = StringField(max_length=30)
    intereses = ListField(ReferenceField(CategoriaPost))
    genero = IntField(default=0)
    edad = IntField(default=0)

class Comunidad(User):
    telefono_contacto = IntField(default=0)
    responsable = StringField(max_length=30)
    a_intereses = ListField(ReferenceField(CategoriaPost))
    
class Amistad(Document):
    seguidor = ReferenceField(User)
    seguido = ReferenceField(User)
    estado = BooleanField(default=False)

class Notificacion(Document):
    destino = ReferenceField('self')
    fuente = ReferenceField('self')
    mensaje = StringField(max_length=120)
    tipo = IntField(default=0)
    vista = IntField(default=0)
    fecha = DateTimeField(default = datetime.datetime.now)


class Perfil (Document):
    userperfil = ReferenceField(User,dbref=False,reverse_delete_rule=CASCADE)
    avatar = StringField(max_length=120,required=True)
    info = StringField(max_length=240,required=True)
   

class Comentario(EmbeddedDocument):
    email_autor = EmailField()
    nombre_autor = StringField(max_length=120)
    texto = StringField(max_length=200)
    fecha_create = DateTimeField(default = datetime.datetime.now)



class Publicacion(Document):
    autor = ReferenceField(User,dbref=False,reverse_delete_rule=CASCADE)
    titulo = StringField(max_length=120, required=True)
    img = StringField(max_length=120)
    contenido = StringField(max_length=500, required=True)
    categoria = ReferenceField(CategoriaPost,required=True)
    fecha_update = DateTimeField(default = datetime.datetime.now)
    tags =ListField(StringField(max_length=30))
    likes = IntField(default = 0)
    comentarios = ListField(EmbeddedDocumentField(Comentario))
    activa = BooleanField(default=True)
    respaldos = ListField(ReferenceField('self'))
    Meta  =  { 
        'ordering' :  [ '-fecha_update' ] 
    }
     