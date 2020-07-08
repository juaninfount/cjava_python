class Rectangulo:

    def __init__(self, base, altura):
        self._base = base
        self._altura = altura
    
    def area(self):
        return self._base*self._altura 
        

rectangulo = Rectangulo(12,3) 
print(rectangulo.area())

rectangulo = Rectangulo(4,5) 
print(rectangulo.area())