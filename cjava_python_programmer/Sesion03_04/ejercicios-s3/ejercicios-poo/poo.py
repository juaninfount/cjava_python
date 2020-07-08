class Persona:
    especie = 'Homo sapiens'
    def __init__(self, nombre, edad):# inicializador/instancia de atribs.
        self.nombre = nombre   # Atributo de clase
        self.edad  = edad

    def __str__(self):
        return 'Nombre:{0}, Edad:{1}'.format(self.nombre, self.edad)
    
    def __repr__(self):
        return 'Persona({0}, Edad:{1})'.format(self.nombre, self.edad)

    def __eq__(self, otro):
        return self.edad == otro.edad

    def hablar(self):
        return 'Hola, mi nombre es %s.' %  (self.nombre)


class Estudiante(Persona):
    hora_dormir = 'medianoche'

    def tarea(self):
        import time
        print('Necesito trabajar')
        time.sleep(5)
        print('Me quedé dormido?')
    
class Empleado(Persona):

    def __init__(self, nombre, edad, empleador):
        super(Empleado, self).__init__(nombre, edad)
        self.empleador = empleador

    def hablar(self):
        conversacion = super(Empleado, self).hablar()
        return conversacion + " Trabajo para {}".format(self.empleador)


jose = Estudiante('Jose',19)
print(jose.especie)
jose.tarea()

fred = Empleado('Pedro Picapiedra', 55, 'Compañía de piedra, roca y grava')
print(repr(fred)) 
print( "Empleador de fred: {0}" .format(fred.empleador) ) 



#print('%s es una persona de %d anhos de edad y con %f cms de estatura.' %  (nadie.nombre, nadie.edad, nadie.estatura) )
#print(nadie.nombre)
#print([method for method in dir(str) if method[:2]=='__'])


