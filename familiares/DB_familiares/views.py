from django.shortcuts import render
from .models import Familiar
from django.http import HttpResponse

def mostrar_familiar(request):
    familiar1= Familiar(nombre="Pablo", apellido="Solis", edad="24", nacimiento='1998-02-03')
    familiar2= Familiar(nombre="Oriana", apellido="Pedromilli", edad="24", nacimiento='1998-09-25')
    familiar3= Familiar(nombre="Tiago", apellido="Solis", edad="18", nacimiento='2004-06-04')

    familiar1.save()
    familiar2.save()
    familiar3.save()

    cadena_de_texto_1= "Familiar guardado:"+' '+familiar1.nombre+" "+familiar1.apellido+", nacido el:"+str(familiar1.nacimiento)+' '+'y tiene'+' '+str(familiar1.edad)
    cadena_de_texto_2= "Familiar guardado:"+' '+familiar2.nombre+" "+familiar2.apellido+", nacido el:"+str(familiar2.nacimiento)+' '+'y tiene'+' '+str(familiar2.edad)
    cadena_de_texto_3= "Familiar guardado:"+' '+familiar3.nombre+" "+familiar3.apellido+", nacido el:"+str(familiar3.nacimiento)+' '+'y tiene'+' '+str(familiar3.edad)
    cadena_de_texto_4= cadena_de_texto_1+'//////////////'+cadena_de_texto_2+'//////////////'+cadena_de_texto_3
    return HttpResponse(cadena_de_texto_4)