
milista = []

def agregar_una_vez(lista, el):
    if lista != None:
        
        if el in lista: # ya se encuentra en la lista
                raise ValueError("Imposible añadir elementos duplicados => [" + str(el)  + "]")                    
        else:
            lista.append(el)
    print(lista)


agregar_una_vez(milista, 10)
agregar_una_vez(milista, -2)
agregar_una_vez(milista, "Hola")
agregar_una_vez(milista, -2)