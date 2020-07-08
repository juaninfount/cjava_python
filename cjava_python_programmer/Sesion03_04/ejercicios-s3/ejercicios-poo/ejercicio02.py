from random import seed
from random import randint
from datetime import datetime

SEXO_DEFECTO = "M"
PESO_IDEAL = -1
PESO_DEBAJO_IDEAL = 0
SOBREPESO = 1

class Persona:
    
    def __init__(self):
        self._nombre = ""
        self._edad = 0
        self._dni = self.generaDNI()
        self._sexo = SEXO_DEFECTO
        self._peso = 0.0
        self._altura = 0.0      
    
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad
 
    @property
    def sexo(self):
        return self._sexo

    @sexo.setter
    def sexo(self, sexo):
        self._sexo = sexo

    @property
    def peso(self):
        return self._peso

    @peso.setter
    def peso(self, peso):
        self._peso = peso

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, altura):
        self._altura = altura    

    def calcular_imc(self):
       imc = PESO_IDEAL
       indicador = (self._peso)/( pow(self._altura,2) )

       if indicador < 20:
           imc = PESO_IDEAL
       elif indicador >= 20 and indicador <= 25:
           imc = PESO_DEBAJO_IDEAL
       else:
           imc = SOBREPESO
       return imc

    def es_mayor_de_edad(self):
        return self._edad >= 18

    def comprobar_sexo(self, sexo):
        return sexo == self._sexo

    # devuelve toda la información del objeto.
    def to_string(self):      
        if self._nombre is not None:                    
            print("Nombre: %s" % self._nombre)

        if self._edad is not None:
            print("Edad: %d" % self._edad)

        if self._dni is not None:
            print("DNI: %s" % self._dni)

        if self._sexo is not None:
            print("Sexo: %s" % self._sexo)

        if self._peso is not None:
            print("Peso: %f" % self._peso)

        if self._altura is not None:
            print("Altura: %f" % self._altura)        
        

    # genera DNI
    def generaDNI(self, cantidad = 8):
        dni = ""
        # seed random number generator
        seed(datetime.now())
        # generate some integers
        for _ in range(cantidad):
	        dni += str(randint(0, 9))  # del 1 al 0

        return dni

class Test:
    persona = None

    def __init__(self):           
        persona = Persona()

        print("Nueva persona")
        persona.nombre = input("Ingresar nombre: ")
        persona.edad = int(input("Ingresar edad: "))
        persona.sexo = input("Ingresar sexo: ")
        persona.peso = float(input("Ingresar peso: "))
        persona.altura = float(input("Ingresar altura: "))        
       
        imc = persona.calcular_imc()
        if imc == PESO_IDEAL:
           print("Peso ideal") 
        elif imc == PESO_DEBAJO_IDEAL:
           print("Peso por debajo del ideal")
        elif imc == SOBREPESO:
           print("Con sobrepeso") 


        if persona.es_mayor_de_edad():
           print("Es mayor de edad")
        else:
           print("Es menor de edad")
        
        print("")
        persona.to_string()

objtest = Test()