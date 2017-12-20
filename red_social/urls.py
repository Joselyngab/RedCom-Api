"""red_social URL Configuration


"""
from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls.static import static
from apps.publicacion import views
from rest_framework import routers

# this is DRF router for REST API viewsets
router = routers.DefaultRouter()

# register REST API endpoints with DRF router
router.register(r'publicacion', views.PublicacionViewSet, r"publicacion")
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^publicacion/', include('apps.publicacion.urls', namespace="publicacion")),

     url(r'^api/', include(router.urls, namespace='api')),
]
