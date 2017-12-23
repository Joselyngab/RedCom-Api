# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from mongoengine import *
import  datetime
#from red_social.settings import DBNAME
#connect(DBNAME)


class User(Document):
    email= EmailField(primary_key=True,unique=True)
    name = StringField(max_length=120)
    apellido = StringField(max_length=30)
    password= StringField(max_length=10)
    intereses = ListField(StringField())
    genero = IntField(default=0)
    edad = IntField(default=0)
    estado = StringField(default="")
    municipio = StringField(default="")
    parroquia = StringField(default="")
    direccion = StringField(default="")
    modificado = DateTimeField(default = datetime.datetime.now)

    
class Amistad(Document):
    seguidor = ReferenceField(User)
    seguido = ReferenceField(User)
    estado = BooleanField(default=False)

class Notificacion(Document):
    destino = ReferenceField('self')
    fuente = ReferenceField('self')
    tipo = IntField(default=0)
    fecha = DateTimeField()

class Perfil (Document):
    userperfil = ReferenceField(User,dbref=False,reverse_delete_rule=CASCADE)
    avatar = StringField(max_length=120,required=True)
    info = StringField(max_length=240,required=True)
    amigos = ListField(ReferenceField(Amistad))

class Comentario(EmbeddedDocument):
    email_autor = EmailField()
    nombre_autor = StringField(max_length=120)
    texto = StringField(max_length=200)
    fecha_create = DateTimeField(auto_now_add=True)

class Imagen(Document):
    url = StringField(max_length=120)
    keyIdP = StringField(max_length=120)
    keyIdPerfil = StringField(max_length=120)

class CategoriaPost(Document):
    nombre= StringField(max_length=60,required=True)

class Publicacion(Document):
    autor = ReferenceField(User,dbref=False,reverse_delete_rule=CASCADE)
    titulo = StringField(max_length=120, required=True)
    contenido = StringField(max_length=500, required=True)
    categoria = ReferenceField(CategoriaPost)
    fecha_update = DateTimeField(auto_now_add=True)
    tags =ListField(StringField(max_length=30))
    likes = IntField(default = 0)
    comentarios = ListField(EmbeddedDocumentField(Comentario))
    Meta  =  { 
        'ordering' :  [ '-fecha_update' ] 
    }
    

class Apoyo(Document):
     usuarioApoya = ReferenceField(User)
     postSeguido = ListField(ReferenceField(Publicacion))