class Ejemplo:

    def publico(self):
        return "Soy un metodo publico, a la vista de todo"

    def __privado(self):
        return "Soy un metodo privado, para ti no existo"


objeto = Ejemplo()
print(objeto.publico())
print(objeto._Ejemplo__privado()) #name mangling
# print(objeto.privado())