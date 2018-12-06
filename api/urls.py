from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^TiendaLista/$', views.TiendaApiShow.as_view()),  
    url(r'^ListaCompras/$', views.ProductoApiShow.as_view()),
]
