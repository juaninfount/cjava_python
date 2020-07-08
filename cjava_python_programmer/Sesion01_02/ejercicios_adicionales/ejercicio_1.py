mi_lista = [1,2,'Hola mundo', True,[5,6,8]]
print(type(mi_lista))
mi_lista.append(7)
print(mi_lista)
print(mi_lista.pop())
mi_lista2  = mi_lista + [4]
print(mi_lista2)

mi_lista.extend([5,6])
print(mi_lista)
print(mi_lista[0])
print(mi_lista[4])