from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):

    return render(request, "DulceDespertarApp/home.html")


def desayunos(request):

    return render(request, "DulceDespertarApp/desayunos.html")


def adicionales(request):

    return render(request, "DulceDespertarApp/adicionales.html")


def tienda(request):

    return render(request, "DulceDespertarApp/tienda.html")


def preguntas_frecuentes(request):

    return render(request, "DulceDespertarApp/preguntas_frecuentes.html")


def contacto(request):

    return render(request, "DulceDespertarApp/contacto.html")