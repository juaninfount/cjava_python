# Pedir dos números y mostrarlos ordenados de mayor a menor.
r1 = float(input("Ingresar primer número: ")) 
r2 = float(input("Ingresar segundo número: ")) 
 
lista = [r1 ,r2]
lista.sort(reverse=True)

print(lista)