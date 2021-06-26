from django.urls import path
from .views import blog, home, agregar_juego, editar_juego, borrar_juego

urlpatterns = [
    path('', home, name="home"),
    path('agregar-juego/', agregar_juego, name="agregar-juego" ),
    path('editar-juego/<pk>/', editar_juego, name="editar-juego" ),
    path('borrar-juego/<pk>/', borrar_juego, name="borrar-juego" ),
   path('blog/', blog, name="blog"),
]