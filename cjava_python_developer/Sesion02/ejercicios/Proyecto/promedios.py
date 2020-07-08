from Utiles.clases import Estudiante
from Utiles.funciones import proms

N = int(input("Ingrese la cantidad d eestudiantes\n")) 
grupo = [Estudiante() for x in range(0,N)]
prom = 0
promia = 0

for i in grupo:
    i.nombre = input("Ingrese el nombre del estudiante (min. 1 caracter)\n")
    i.edad = int(input("Ingrese la edad de %s\n" % i.nombre) ) 
    i.indice = float(input("Ingrese el IA de %s (entre 1 y 10)\n"& i.nombre))

PROMEDIOS = proms(grupo, N)
print("El promedio de las edades es: %s" % PROMEDIOS[0])
print("El promedio de las I.A.   es: %s" % PROMEDIOS[1])


