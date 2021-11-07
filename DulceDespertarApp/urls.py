from django.urls import path
from DulceDespertarApp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.home, name="Home"),
    path('adicionales',views.adicionales, name="Adicionales"),
    path('tienda',views.tienda, name="Tienda"),
    path('preguntas_frecuentes',views.preguntas_frecuentes, name="Preguntas Frecuentes"),
    path('contacto',views.contacto, name="Contacto"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)