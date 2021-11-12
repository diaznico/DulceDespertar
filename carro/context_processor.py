from .carro import Carro

def importe_total_carro(request):

    total=0
    if request.user.is_authenticated:
        if request.session["carro"]:
            for key, value in request.session["carro"].items():
                total+=int(value["precio"])

    return {"importe_total_carro" : total}