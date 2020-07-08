
def es_vocal(letra):
    if  letra is not None:
        letra = letra.upper() 
        if letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':
            return True

    return False

print(es_vocal('A'))
print(es_vocal('d'))
print(es_vocal('e'))