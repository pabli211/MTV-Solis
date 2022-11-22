from django.shortcuts import render
from .models import Familiar
from django.http import HttpResponse

def mostrar_familiar(request):
    familiar1= Familiar(nomrbe="Pablo", apellido="Solis", edad="24", nacimiento='3-2-98')
    familiar2= Familiar(nomrbe="Oriana", apellido="Pedromilli", edad="24", nacimiento="25-9-98")
    familiar3= Familiar(nomrbe="Tiago", apellido="Solis", edad="18", nacimiento='4-6-04')

    familiar1.save()
    familiar2.save()
    familiar2.save()

    cadena_de_texto_1= "Familiar guardado:"+' '+familiar1.nombre+" "+familiar1.apellido+", nacido el:"+familiar1.nacimiento+' '+'y tiene'+' '+familiar1.edad
    cadena_de_texto_2= "Familiar guardado:"+' '+familiar2.nombre+" "+familiar2.apellido+", nacido el:"+familiar2.nacimiento+' '+'y tiene'+' '+familiar2.edad
    cadena_de_texto_3= "Familiar guardado:"+' '+familiar3.nombre+" "+familiar3.apellido+", nacido el:"+familiar3.nacimiento+' '+'y tiene'+' '+familiar3.edad

    return HttpResponse(cadena_de_texto_1, cadena_de_texto_2,cadena_de_texto_3)