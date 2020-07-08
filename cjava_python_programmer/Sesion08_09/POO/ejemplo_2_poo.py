class MiPerro:
    """ Segundo ejemplo """

    def __init__(self, raza):
        self.raza = raza

    def ladrar(self, ladrido):
        print(ladrido)

    def juego(self, jugar):
        print(jugar)

    def proteger(self, cuidar):
        print(cuidar)

""" Instanciamos dos objetos de la clase mi perro """            
bobi = MiPerro("Pastor Aleman")
firulais = MiPerro("dalmata")

"""  Accedemos al atributo """
print(bobi.raza)
print(firulais.raza)

""" Accederemos a los metodos """
bobi.ladrar("guau guau, me llamo bobi")
firulais.ladrar("guau guau, me llamo firulais")

