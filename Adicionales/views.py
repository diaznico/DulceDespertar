from django.shortcuts import render
from Adicionales.models import adicionales

# Create your views here.

def adicionales1(request):

    adicional_s = adicionales.objects.all()

    return render(request, "Adicionales/adicionales.html", {"adicional_s": adicional_s})