def numeros_amigo(x,y):
    div_x=0
    for i in range(1,round(x/2)+1):
        if x % i == 0:
            #print(i)
            div_x=div_x+i
    #print(div_x)
    div_y=0
    for i in range(1,round(y/2)+1):
        if y % i == 0:
            #print(i)
            div_y=div_y+i
    #print(div_y)
    if (div_x == y) and (div_y == x):
        print(f"{x} es AMIGO de {y}")
    else:
        print(f"{x} es NO AMIGO de {y}")
a = int(input("Numero 1: "))
b = int(input("Numero 2: "))
numeros_amigo(a,b)