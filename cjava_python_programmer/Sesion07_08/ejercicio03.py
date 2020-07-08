# Ejercicio 3: Escribir una función que simule una calculadora científica que permita 
# calcular el seno, coseno, tangente, exponencial y logaritmo neperiano. La función preguntará
#  al usuario el valor y la función a aplicar, y mostrará por pantalla una tabla con los enteros
#  de 1 al valor introducido y el resultado de aplicar la función a esos enteros.

import math

def funcion_matematica():
    numero = int(input("Ingresar un valor entero: "))
    id_funcion = input("Ingresar la función a aplicar (sin, cos, tan, exp, log): ")

    for i in range(1,numero+1):

        if id_funcion == 'sin':
           print('sin(%d) = %f ' % (i , math.sin(i))) 
        if id_funcion == 'cos':
           print('cos(%d) = %f ' % (i , math.cos(i)))
        if id_funcion == 'tan':
           print('tan(%d) = %f ' % (i , math.tan(i)))
        if id_funcion == 'exp':
           print('exp(%d) = %f ' % (i , math.exp(i)))
        if id_funcion == 'log':
           print('log(%d) = %f ' % (i , math.log(i)))



funcion_matematica()
    