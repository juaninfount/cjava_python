
#Ejercicio 1: Escribir que reciba una frase y devuelva un diccionario con las palabras que contiene y su longitud.

def diccionario(frase):

    diccionario = {}
    lstPalabras = frase.split()
    for item in lstPalabras:
        diccionario[item] = len(item)
    
    return diccionario

        
print(diccionario("Este es un texto de prueba"))    