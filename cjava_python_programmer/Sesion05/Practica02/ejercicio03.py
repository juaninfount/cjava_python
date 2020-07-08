class OperadorCadena:

    def __init__(self):
        self._cadena = ""
    
    def get_string(self):
        self._cadena = input("Ingresar una cadena: ")
    
    def print_string(self):
        print(self._cadena.upper())



objOperadorCadena = OperadorCadena()
objOperadorCadena.get_string()
objOperadorCadena.print_string()