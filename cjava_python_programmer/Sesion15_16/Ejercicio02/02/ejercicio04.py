import sys

def suma_enteros(a,b):
    return "a+b = %d" % (a+b)
    
try:
    a = 1
    b = [2.3]

    print(  str(type(b)) )
    if 'int' not in str(type(a)):
        raise TypeError('Valor a no es tipo entero.')

    if 'int' not in str(type(b)):
        raise TypeError('Valor b no es tipo entero.')

    print(suma_enteros(a, b)) 
except TypeError as error:
    print( "{} -> Error de tipo de datos, a={}, b={}".format( str(error) , a, b))






