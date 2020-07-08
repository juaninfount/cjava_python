from random import seed
from random import randint
from datetime import datetime


MIN_CHAR_MAY = 3
MIN_CHAR_MAY = 2
MIN_CHAR_NUM = 6

class Password:
        
    _mayusculas = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    _minusculas = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    _numeros    = ['0','1','2','3','4','5','6','7','8','9']
    
    def __init__(self, longitud):
        self._longitud = longitud
        self._contrasenha = self.generarPassword()
        self._es_fuerte = False

    def generarPassword(self):
        lenMay = len(self._mayusculas) 
        lenMin = len(self._minusculas) 
        lenNum = len(self._numeros)
        password = []

        seed(datetime.now())
        for _ in range(self._longitud):
            posMay = randint(0, lenMay - 1)  # del 0 a la lenMay - 1, para extraer mayusculas
            posMin = randint(0, lenMin - 1)  # del 0 a la lenMin - 1, para extraer mayusculas
            posNum = randint(0, lenNum - 1)  # del 0 a la lenNum - 1, para extraer numeros
             
        return ""

    def setLongitud(self,longitud):
        self._longitud = longitud
    
    def getLongitud(self):
        return self._longitud 

    def getContrasenha(self):
        return self._contrasenha

    def esFuerte(self):
        return True

    def setFuerte(self):
        self._es_fuerte = True    