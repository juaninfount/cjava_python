lista = []
n = int(input("Numero: "))
while n != 0:
    lista.append(n)
    n = int(input("Numero: "))
suma=0
for i in lista:
     suma=suma+i
print(suma)