class Ejemplo:

    def __init__(self):
        self.__oculto = "Me encuentro oculto de la clase"
    
    def publico(self):
        return "Soy un método pùblico, a la vista de todo"

    def __privado(self):
        return "Soy un método privado, para ti no existo"

    def get_oculto(self):
        return self.__oculto

    def set_oculto(self):
        self.__oculto = self.__privado()

objeto = Ejemplo()
print(objeto.publico())
print(objeto._Ejemplo__privado()) #name mangling
print(objeto.get_oculto())
objeto.set_oculto()
print(objeto.get_oculto())
# print(objeto.privado())