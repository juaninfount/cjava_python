from tkinter import *

def saludar():
    print("Hola: " + nombre.get() + " " + apellidoP.get() + " " + apellidoM.get())

ventana = Tk()
nombre = StringVar()
apellidoP = StringVar()
apellidoM = StringVar()
edad = StringVar()
sexo = StringVar()

nombre.set("Escribe tu nombre")
ventana.title("Entradas en tkinter")
ventana.geometry("400x200")
Label(ventana, text="Escribe tu nombre: ").place(x=10,y=10)
Entry(ventana, textvariable=nombre).place(x=170, y=10)
Label(ventana, text="Escribe tu apellido paterno: ").place(x=10,y=40)
Entry(ventana, textvariable=apellidoP).place(x=170, y=40)
Label(ventana, text="Escribe tu apellido materno: ").place(x=10,y=70)
Entry(ventana, textvariable=apellidoM).place(x=170, y=70)

Label(ventana, text="Edad: ").place(x=10,y=100)
Entry(ventana, textvariable=edad).place(x=50, y=100)
Label(ventana, text="Sexo: ").place(x=10,y=130)
Entry(ventana, textvariable=sexo).place(x=50, y=130)
Button(ventana, text="Saludo personalizado", command=saludar).place(x=50,y=160)

Label(ventana)
ventana.mainloop()


