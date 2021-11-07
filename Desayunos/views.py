from django.shortcuts import render
from Desayunos.models import desayunos


# Create your views here.

def desayunos1(request):

    servicios = desayunos.objects.all()

    return render(request, "Desayunos/desayunos.html", {"servicios": servicios})
