from django.conf import settings
# from django.conf.urls import pa 
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.management import execute_from_command_line
from django.template import Template, Context
from django import forms
import datetime
import sys
import os


class Contacto(forms.Form):
    nombre = forms.CharField(max_length=100, label='Nombre')
    edad = forms.IntegerField(label='Edad')    
    direccion = forms.CharField(max_length=100, label='Direccion')

# def saludo(request):
#     """Con retorno de texto"""
#     #return HttpResponse("Hola alumnos, ésta es una segunda página con django")
#     documento = """ 
#                 <html>
#                 <body>
#                 <h1>Hola alumnos, ésta es nuestra primera página con django</h1>
#                 </body>
#                 </html>
#                 """
#     return HttpResponse(documento)

def saludo(request): 
    """Con plantilla"""

    form = Contacto()  
    submitted = False
    if request.method == "POST":
        data = request.POST.copy()
        nombre = data.get('nombre')
        edad = data.get('edad')
        direccion = data.get('direccion')
        submitted = True
        return HttpResponse( "Sr(a) %s, tiene %i años de edad y vive en %s." % ( nombre, int(edad) , direccion) )
        #     {
        #         'nombre': '',
        #         'submitted':True
        #     }
        # )
               
    return render(request,'miplantilla.html',{
                'form': form, 'submitted':submitted
    })

def despedida(request):
    return HttpResponse("Hasta luego, alumnos django")

def damefecha(request):
    fecha_actual = datetime.datetime.now()
    documento = """
                <html>
                            <body>
                            <h1>Fecha y Hora actuales</h1> %s
                            </body>
                </html>
                """ % fecha_actual
    return HttpResponse(documento)

def calculaedad(request, anho):
    edadactual = 18
    periodo = anho - int(datetime.datetime.today().year) 
    edadfutura = edadactual + periodo
    documento = """
                <html>
                            <body>
                            <h2>En el año %s tendrás %s años</h2> 
                            </body>
                </html>
                """ % (anho , edadfutura)
    return HttpResponse(documento)


if __name__ == "__main__":
    execute_from_command_line(sys.argv)