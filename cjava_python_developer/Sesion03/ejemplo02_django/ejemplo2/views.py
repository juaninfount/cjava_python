from django.http import HttpResponse
from datetime import datetime

def saludo(request):
    return HttpResponse("Hello world!")

def despedida(request):
    return HttpResponse("Hasta luego, alumnos django")

def damefecha(request):    
    fecha_actual = datetime.now()
    documento = """
                <html>
                            <body>
                            <h1>Fecha y Hora actuales</h1> %s
                            </body>
                </html>
                """ % fecha_actual
    return HttpResponse(documento)