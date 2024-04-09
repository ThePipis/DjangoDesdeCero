from django.http import HttpResponse
import datetime
from django.template import Template, Context

class Persona(object):
    def __init__(self, nombre, apellido):
      self.nombre = nombre
      self.apellido = apellido

def saludo(request):
    p1=Persona("Profesor Jose","Gonzales")
    ahora = datetime.datetime.now() 
    temas_curso=[]
    doc_externo = open("D:/Django-React/CursoPythonDjango/DjangoDesdeCero/proyecto1/plantillas/miplantilla.html")
    plt=Template(doc_externo.read())
    doc_externo.close()
    ctx=Context({'nombre_persona': p1.nombre, 'apellido': p1.apellido,'momento_actual':ahora,'temas':temas_curso})
    documento=plt.render(ctx)
    return HttpResponse(documento)

def despedida(request):
    return HttpResponse("Hasta luego Django")

def dameFecha(request):
    fecha_actual = datetime.datetime.now() 
    documento="""<html>
    <body>
    <h1>Fecha y Hora Actuales: %s </h1> 
    </body>
    </html>""" %fecha_actual    
    return HttpResponse(documento)

def calculaEdad(request,agno,edad):
    periodo=agno-2024
    edadFutura=edad+periodo
    documento="""<html>
    <body>
    <h2>En el año %s tendras %s años.</h2>
    </body>
    </html>""" % (agno,edadFutura)
    return HttpResponse(documento)    