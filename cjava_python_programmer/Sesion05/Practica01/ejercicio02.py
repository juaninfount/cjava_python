
def maximo(a,b):
    
    if (a > b):
        return a
    elif (b > a):
        return b
    
    return None
 

a = 11
b = 10
x = maximo(a,b)

print("Máximo : " + str(x))