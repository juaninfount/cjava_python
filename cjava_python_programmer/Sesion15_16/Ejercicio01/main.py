import math

class Punto:

    def __init__(self, x, y):
        """
        Constructor de objeto Punto, con sus coordenadas x e y.
        """
        self._x = x
        self._y = y

    def __str__(self): 
        """
        Sobrescritura del metodo __str__ para imprimir el punto en formato (x,y)
        """
        return '(%f,%f)' % (self._x, self._y)

    def cuadrante(self):
        """
        Metodo que indica a que cuadrante pertenece el punto.
        """

        if self._x == 0 and self._y != 0:
            return "Eje Y"
        elif self._x != 0 and self._y == 0:
            return "Eje X"
        elif self._x == 0 and self._y == 0:
            return "Origen 0"
        elif self._x > 0 and self._y > 0:
            return "Cuadrante I (+X,+Y)"
        elif self._x < 0 and self._y > 0:
            return "Cuadrante II (-X,+Y)"
        elif self._x < 0 and self._y < 0:
            return "Cuadrante III (-X,-Y)"
        elif self._x > 0 and self._y < 0:
            return "Cuadrante IV (+X,-Y)"
        
        return ""

    def vector(self, Q):
        """vector entre dos puntos PQ, donde p es el punto inicial y Q el punto destino.
            Resta abscisas y ordenadas de cada punto.
                            PQ -> = Q - P 
            = (q_1 - p_1, q_2 - p_2)
        """

        vector = Punto(Q._x - self._x, Q._y - self._y)
        return str(vector) 
    
    def distancia(self, Q):
        """ 
        Añade un método llamado distancia, que tome otro punto y calcule la distancia entre los dos puntos y la 
        muestre por pantalla. La fórmula es la siguiente:
                            d = sqrt( (x_2 - x_1)^2 + (y_2 - y_1)^2 )
        """
        
        return math.sqrt(pow(Q._x - self._x,2) - pow(Q._y - self._y,2)) 
        
if __name__ == "__main__":
    P = Punto(12,3)
    Q = Punto(1,-6)

    print(P.cuadrante()) 
    print(P.distancia(Q))
    print(P.vector(Q))
