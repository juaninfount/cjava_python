import math

class Circulo:

    def __init__(self, radio):
        print("Radio circulo: " , str(radio))
        self._radio = radio        
    
    def area(self):
        return pow(self._radio,2) * math.pi

    def perimetro(self):
        return 2*self._radio*math.pi
        
r = 3
circulo = Circulo(r) 
print("Area: {0:.2f}" .format(round(circulo.area(),3)) )
print("Perímetro: {0:.2f}".format(round(circulo.perimetro(),3)) )

r = 4
circulo = Circulo(r) 
print("Area: {0:.2f}" .format(round(circulo.area(),3)) )
print("Perímetro:  {0:.2f}".format(round(circulo.perimetro(),3)) )
