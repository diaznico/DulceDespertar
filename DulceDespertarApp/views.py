from django.shortcuts import render, HttpResponse



# Create your views here.

def home(request):

    return render(request, "DulceDespertarApp/home.html")





def preguntas_frecuentes(request):

    return render(request, "DulceDespertarApp/preguntas_frecuentes.html")