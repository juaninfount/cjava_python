# Leer números hasta que se introduzca un 0. Para cada uno indicar si es par o impar.

r = int(input("Ingresar un número: "))  

while r != 0:
    if r % 2 == 0:
        print("Número par")
    else:
        print("Número impar")

    r = int(input("Ingresar un número: "))  

print("Cero ingresado")