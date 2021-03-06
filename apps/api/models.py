# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings

from mongoengine_extras.fields import AutoSlugField
from django.template import defaultfilters
from mongoengine import *
import datetime
connect ( db ='redcom' ) 


	
class CategoriaPost(Document):
    nombre = StringField(max_length=50,required=True, unique=True)
    fecha_create = DateTimeField(default = datetime.datetime.now)
    activa = BooleanField(default=True)

class Perfil (EmbeddedDocument):
    avatar = StringField(max_length=120,required=True)
    info = StringField(max_length=240,required=True)
    estado = StringField(max_length=120)

class User(Document):
    email =StringField(unique=True, required=True)
    slug =  AutoSlugField(populate_from=email)
    name = StringField(max_length=120)
    password= StringField(max_length=10)
    estado = StringField(default="",required=False)
    ciudad = StringField(default="",required=False)
    direccion = StringField(default="",required=False)
    seguidores = ListField(StringField(null=True,required=False))
    seguidos = ListField(StringField(null=True,required=False))
    notificaciones = ListField(StringField(null=True,required=False))
    userperfil =  EmbeddedDocumentField(Perfil)
    modificado = DateTimeField(default = datetime.datetime.now, null=True,required = False)
    activo = BooleanField(default=True)
    meta = {'allow_inheritance': True,
     'ordering' :  [ '-fecha_update' ] 
     }
    def save(self, *args, **kwargs):
           if not self.id:
            self.slug = defaultfilters.slugify(self.email)
            super(User, self).save(*args, **kwargs)

class Ente(User):
    telefono = IntField(default=0, min_value=11)
    area_dedicada = StringField()

class Persona(User):
    apellido = StringField(max_length=30)
    intereses = ListField(StringField(),null=True)
    genero = IntField(default=0)
    edad = IntField(default=0)

class Comunidad(User):
    telefono_contacto = IntField(default=0)
    responsable = StringField(max_length=30)
    a_intereses = ListField(StringField(), null=True)
    
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
    estado = StringField(default="",required=False)
    ciudad = StringField(default="",required=False)
    direccion = StringField(default="",required=False)
    fecha_update = DateTimeField(default = datetime.datetime.now,null=True,required = False)
    tags =ListField(StringField(max_length=30),null=True)
    likes = IntField(default = 0,null=True)
    comentarios = ListField(EmbeddedDocumentField(Comentario),null=True,required = False)
    activa = BooleanField(default=True,null=True)
    respaldos = ListField(StringField(),null=True)
    Meta  =  { 
        'ordering' :  [ '-fecha_update' ] 
    }

class Municipio(EmbeddedDocument):
    municipio = StringField(max_length=60)
    capital = StringField(max_length=60)
    parroquias = ListField(StringField(max_length=60))   

class Estado(Document):
    iso_31662 = StringField(max_length=100)
    estado = StringField(max_length=30)
    capital = StringField(max_length=60)
    id_estado = IntField(unique=True)
    municipios = ListField(EmbeddedDocumentField(Municipio))
    ciudades = ListField(StringField(max_length=60))
