# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
#from apps.usuario import models
# Create your models here.
#from usuario.models import User
from mongoengine import *
#from red_social.settings import DBNAME
#connect(DBNAME)
class User(Document):
      name = StringField(max_length=120)

class Comentario(EmbeddedDocument):
    nombreUser = StringField(max_length=120)
    contenidoc = StringField(max_length=200)
    fecha_create = DateTimeField()

class Imagen(Document):
    url = StringField(max_length=120)
    keyIdP = StringField(max_length=120)
    keyIdPerfil = StringField(max_length=120)

class Publicacion(Document):
    autor = ReferenceField('User',dbref=False,reverse_delete_rule='CASCADE')
    img = ReferenceField('Imagen')
    titulo = StringField(max_length=120, required=True)
    contenido = StringField(max_length=500, required=True)
    fecha_update = DateTimeField(required=True)
    tags =ListField(StringField(max_length=30))
    apoyo = IntField(default = 0)
    comentarios = MapField(EmbeddedDocumentField('Comentario'))



