def enteros_cuadrados(lst):
    lst_2 = []
    for i in lst:
        lst_2.append(pow(i,2))  
    
    return lst_2

print(enteros_cuadrados([1,33,45,5,6,4]))