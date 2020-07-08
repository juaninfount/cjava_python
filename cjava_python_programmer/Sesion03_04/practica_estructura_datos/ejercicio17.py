# Escribir una función que calcule el máximo común divisor de dos números. 
def mcd(a,b):  
    if b == 0:
        return a
    else:
        return mcd(b, a % b)


'''
a = int(input("Ingresar primer número: ")) 
b = int(input("Ingresar segundo número: ")) 
r = mcd(a,b)
print("Resultado del M.C.D de dos números: %d" % r)
'''