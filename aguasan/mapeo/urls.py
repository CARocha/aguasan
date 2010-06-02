from django.conf.urls.defaults import *
from django.conf import settings
from models import *


urlpatterns = patterns('mapeo.views',
    (r'^index/$', 'index'),
    (r'^mapeo/formulario/$', 'formulario'),
    (r'^mapeo/mapa/$', 'mapa'),
    (r'^mapeo/mapa/departamento/(?P<id>\d+)/$', 'departamento'),
    (r'^proyecto/(?P<id>\d+)/$', 'proyecto'),
    (r'^proyecto/(?P<id>\d+)/donantes/$', 'donantes_proyecto'),
    (r'^proyecto/(?P<id>\d+)/contrapartes/$', 'contrapartes_proyecto'),
    (r'^proyecto/(?P<id>\d+)/departamento/$', 'departamento_proyecto'),
    (r'^proyecto/(?P<id>\d+)/fotos/$', 'fotos_proyecto'),
    (r'^proyecto/(?P<id_proyecto>\d+)/departamento/(?P<id_dept>\d+)/municipio$', 'municipio_proyecto'),
    (r'^proyectos/$', 'lista_proyectos'),
    (r'^proyectos/donantes/(?P<id_donante>\d+)/$', 'proyectos_donante'),
    (r'^proyectos/donantes/$', 'lista_donantes',  {'template_name': 'mapeo/boton_donante.html'}),
    (r'^proyectos/contrapartes/(?P<id_contraparte>\d+)/$', 'proyectos_contraparte'),
    (r'^proyectos/contrapartes/$', 'lista_contrapartes',  {'template_name': 'mapeo/boton_contraparte.html'}),
    (r'^proyectos/municipio/(?P<id_municipio>\d+)/$', 'proyectos_municipio'),
    (r'^proyectos/editar/(?P<id>\d+)/$', 'editar_proyecto'),
    (r'^donantes/$', 'lista_donantes',  {'template_name': 'mapeo/lista_donantes.html'}),
    (r'^donantes/agregar/$', 'agregar_donante'),
    (r'^donantes/editar/(?P<id>\d+)/$', 'editar_donante'),
    (r'^contrapartes/$', 'lista_contrapartes', {'template_name': 'mapeo/lista_contrapartes.html'}),
    (r'^contrapartes/agregar/$', 'agregar_contraparte'),
    (r'^contrapartes/editar/(?P<id>\d+)/$', 'editar_contraparte'),
    (r'^ajax/agregar/contraparte/(?P<id>\d+)/$', 'agregar_contraparte_proyecto'),
    (r'^ajax/eliminar/contraparte/(?P<id>\d+)/$', 'eliminar_elemento_proyecto', {'model': ProyectoContraparte}),
    (r'^ajax/agregar/donante/(?P<id>\d+)/$', 'agregar_donante_proyecto'),
    (r'^ajax/eliminar/donante/(?P<id>\d+)/$', 'eliminar_elemento_proyecto', {'model': ProyectoDonante}),
    (r'^ajax/agregar/departamento/(?P<id>\d+)/$', 'agregar_departamento_proyecto'),
    (r'^ajax/eliminar/departamento/(?P<id>\d+)/$', 'eliminar_elemento_proyecto', {'model': ProyectoDepartamento}),
    (r'^ajax/agregar/municipio/(?P<id_proyecto>\d+)/(?P<id_dept>\d+)/$', 'agregar_municipio_proyecto'),
    (r'^ajax/eliminar/municipio/(?P<id>\d+)/$', 'eliminar_elemento_proyecto', {'model': ProyectoMunicipio}),
    (r'^ajax/eliminar/foto/(?P<id>\d+)/$', 'eliminar_elemento_proyecto', {'model': ProyectoFotos}),
    (r'^ajax/lista/donantes/(?P<id>\d+)/$', 'lista_donantes_proyecto'),
    (r'^ajax/lista/contrapartes/(?P<id>\d+)/$', 'lista_contrapartes_proyecto'),
    (r'^ajax/lista/lugares/(?P<id>\d+)/$', 'lista_lugares'),
    (r'^ajax/lista/fotos/(?P<id>\d+)/$', 'lista_fotos_proyecto'),
)
