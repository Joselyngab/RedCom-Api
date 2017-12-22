# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from mongoengine import *
#from red_social.settings import DBNAME
#connect(DBNAME)


class User(Document):
    name = StringField(max_length=120,required=True)
    apellido = StringField(max_length=30, required=True)
    email= EmailField(primary_key=True)
    password= StringField(max_length=10,required=True)
    intereses = ListField(StringField(),required=True)
    genero = BooleanField(required=True)
    estado = StringField()
    municipio = StringField()
    parroquia = StringField()
    direccion = StringField()
    edad = IntField(default=0)
   
    
class Amistad(Document):
    seguidor = ReferenceField(User)
    seguido = ReferenceField(User)
    estado = BooleanField(default=False)

class Notificacion(Document):
    destino = ReferenceField(User)
    fuente = ReferenceField(User)
    tipo = IntField(default=0)
    fecha = DateTimeField()

class Perfil (Document):
    userperfil = ReferenceField(User,dbref=False,reverse_delete_rule=CASCADE)
    avatar = StringField(max_length=120,required=True)
    info = StringField(max_length=240,required=True)
    amigos = ListField(ReferenceField(Amistad))

class Comentario(EmbeddedDocument):
    nombreUser = StringField(max_length=120)
    contenidoc = StringField(max_length=200)
    fecha_create = DateTimeField()

class Imagen(Document):
    url = StringField(max_length=120)
    keyIdP = StringField(max_length=120)
    keyIdPerfil = StringField(max_length=120)

class CategoriaPost(Document):
    nombre= StringField(max_length=60,required=True)

class Publicacion(Document):
    autor = ReferenceField(User,dbref=False,reverse_delete_rule=CASCADE)
    img = ReferenceField(Imagen)
    titulo = StringField(max_length=120, required=True)
    contenido = StringField(max_length=500, required=True)
    fecha_update = DateTimeField(required=True)
    tags =ListField(StringField(max_length=30))
    apoyo = IntField(default = 0)
    comentarios = MapField(EmbeddedDocumentField(Comentario))
    categoria = ReferenceField(CategoriaPost)

class Apoyo(Document):
     usuarioApoya = ReferenceField(User)
     postSeguido = ListField(ReferenceField(Publicacion))