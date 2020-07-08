# 19. Diseña una función que decida si un número es primo.
import ejercicio17

r = int(input("Ingresar número: "))
numeroPrimo = True
for i in range(1,r):
     if ejercicio17.mcd(i,r) != 1:
        numeroPrimo = False
        print("Numero no primo")
        break

if numeroPrimo and r != 1:    
    print("Numero primo")
else:
    print("Numero 1")