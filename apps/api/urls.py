from django.conf.urls import url,include
from views import index,update,delete

urlpatterns = [
    url(r'^index$', index),
     url(r'^borrar$', delete),
      url(r'^actualizar$', update),
]
