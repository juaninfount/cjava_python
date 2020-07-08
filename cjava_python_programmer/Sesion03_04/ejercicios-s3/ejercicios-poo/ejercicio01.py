class Cuenta:  
    titular = ""
    cantidad = 0.0

    def __init__(self,titular,cantidad=0.0):
        self.titular = titular
        if cantidad != 0:
            self.cantidad = cantidad

    def getTitular(self):
        return self.titular

    def setTitular(self,x):
        self.titular = x

    def getCantidad(self):
        return self.cantidad

    def setCantidad(self,cantidad):
        self.cantidad = cantidad

    def ingresar(self, adicional):
        if adicional >= 0:
            self.cantidad = self.cantidad + adicional

    def retirar(self,retiro):
        self.cantidad = self.cantidad - retiro
        if self.cantidad < 0:
           self.cantidad = 0
        
    def ToString(self):
        return self.titular + ", saldo: " + str(self.cantidad) 



micuenta = Cuenta("Juan")
micuenta.ingresar(10.0)
print("Saldo actual ","{0:.2f}".format(micuenta.getCantidad()) ) 
micuenta.retirar(5.0)
print("Saldo actual ","{0:.2f}".format(micuenta.getCantidad()) ) 
print(micuenta.ToString())

        