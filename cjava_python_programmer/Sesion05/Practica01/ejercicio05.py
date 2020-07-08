diccionario ={}
entrada = input('Ingrese una cadena: ')

for w in entrada.split(" "):
     diccionario[w] = len(w)   
    
print(diccionario)