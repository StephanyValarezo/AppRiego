from django.shortcuts import render
from django.shortcuts import render, HttpResponse
from webAppW.models import Sensores
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Sensores, Valvulas
from rest_basic.serializers import SensoresSerializer
from django.views.decorators.csrf import csrf_exempt
from webAppW.forms import FormularioEstado
from rest_basic.models import Valvulas_Water


# Create your views here.

#funcion para renderizar Inicio
def inicio(request):

    return render(request, "index.html")

#Funcion para renderizar la pagina de valvulas
def valvulaVentana(request):

    valvulas= Valvulas_Water.objects.all()

    sensores = Sensores.objects.all()

    renderingObject = {"sensores": sensores, "valvulas": valvulas}

    if request.method=="GET":
        
        return render(request, "valvulaswindow.html", renderingObject)

    #Aqui guardo el valor del estado de mis valvulas en la base de datos
    elif request.method == "POST":

        listaEstados1 = request.POST.getlist("1") #obtengo el valor de mi toggle boton de la pagina valvulas

        listaEstados2 = request.POST.getlist("2")
        
        #Aqui guardo el valor del boton ya presionado para las dos valvulas
        try:
            if "on" in listaEstados1:
                t = Valvulas_Water.objects.get(id=1)
                t.state = True
                t.save()

            else:
                t = Valvulas_Water.objects.get(id=1)
                t.state = False
                t.save()

            if "on" in listaEstados2:
                t = Valvulas_Water.objects.get(id=2)
                t.state = True
                t.save()

            else:
                t = Valvulas_Water.objects.get(id=2)
                t.state = False
                t.save()
            
            #Aqui vuelvo actualizar mis datos, estads, nombre de la valvula
            valvulas= Valvulas_Water.objects.all()

            renderingObject["valvulas"]=valvulas
        
            renderingObject["showSuccesText"] = True #Si todo esta bien sale un mensaje de que si se realizaron los cambios

        except:

            renderingObject["showErrorText"] = True #si algo va mas sale el mensaje de que no se pudo realizar los cambios

        return render(request, "valvulaswindow.html", renderingObject)
        
    else:

        return render(request, "valvulaswindow.html",renderingObject)
    




