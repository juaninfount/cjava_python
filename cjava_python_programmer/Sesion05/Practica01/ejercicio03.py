
edad = input("Ingresar su edad: ") 

while True:
    if  edad.isdigit(): 
        edad = int(edad)
        if edad < 18:
            print("No es mayor de edad")
        elif  edad >= 18:
            print("Es mayor de edad")
        break
    else:
        edad = input("Entrada no válida. Reingresar edad: ")
