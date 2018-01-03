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

class Perfil (Document):
    avatar = StringField(max_length=120,required=True)
    info = StringField(max_length=240,required=True)
    estado = StringField(max_length=120)

class User(Document):
    email =StringField(unique=True, required=True)
    slug =  AutoSlugField(populate_from=email)
    name = StringField(max_length=120)
    password= StringField(max_length=10)
    estado = StringField(default="")
    ciudad = StringField(default="")
    direccion = StringField(default="")
    seguidores = ListField(ReferenceField('self'))
    seguidos = ListField(ReferenceField('self'))
    notificaciones = ListField(ReferenceField('self'))
    userperfil = ReferenceField(Perfil,dbref=False,reverse_delete_rule=CASCADE)
    modificado = DateTimeField(default = datetime.datetime.now)
    activo = BooleanField(default=True)
    token = StringField(max_length=120)
    meta = {'allow_inheritance': True,
     'ordering' :  [ '-fecha_update' ] 
     }
    def save(self, *args, **kwargs):
           if not self.id:
            self.slug = defaultfilters.slugify(self.email)
            super(User, self).save(*args, **kwargs)

class Ente(User):
    telefono = IntField(default=0, min_value=11)
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
