# Pedir un número entre 0 y 9999 y decir cuántas cifras tiene.
r = int(input("Ingresar un número: "))  
if r >= 0 and r <= 9999:    
    strvar = str(r)
    print("Cifras %d:" % len(strvar))
else:
    print("Número no permitido")