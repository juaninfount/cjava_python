import math 

print('Ingresar coeficientes de una ecuación de 2do grado: ax^2 + bx + c = 0')
a = float(input("a: ")) 
b = float(input("b: "))
c = float(input("c: "))


x1 = (-b +  (math.sqrt( pow(b,2) - 4*a*c ) ))/2*a
x2 = (-b -  (math.sqrt( pow(b,2) - 4*a*c ) ))/2*a

print("Los resultados son") # x1: %8.2f y x2: %8.2f" % x1, x2)
print(x1)
print(x2)
