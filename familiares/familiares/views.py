from django.template import Template, context, loader
from django.http import HttpResponse

def probando_html(request):
    nom="Pablo"
    ap= "Solis"

    diccionario={"nombre":nom, "apellido":ap}

    plantilla= loader.get_template('template.html')
    documento= plantilla.render(diccionario)
    return HttpResponse(documento)