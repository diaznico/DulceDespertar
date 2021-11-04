from django.urls import path
from DulceDespertarApp import views


urlpatterns = [
    path('',views.home, name="Home"),
    path('desayunos',views.desayunos, name="Desayunos"),
    path('adicionales',views.adicionales, name="Adicionales"),
    path('tienda',views.tienda, name="Tienda"),
    path('preguntas_frecuentes',views.preguntas_frecuentes, name="Preguntas Frecuentes"),
    path('contacto',views.contacto, name="Contacto"),
]
