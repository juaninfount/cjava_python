class OperadorCadena:
  
    def revertir_cadena(self, cadena_original):        
        cadena_invertida=""
        lista_orig = cadena_original.split(" ")
       
        i = len(lista_orig) 
        while i > 0: 
            cadena_invertida += lista_orig[i-1] + " "
            i = i - 1
        
        return str(cadena_invertida.strip())


operador = OperadorCadena()
print(operador.revertir_cadena("Mi Diario Python"))