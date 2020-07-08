from tkinter import *

def obtener():
    print(valor.get())


ventana = Tk()
valor = StringVar()
ventana.title("Uso de spinbox con tkinter")
ventana.geometry("400x300")
Label(ventana, text="Ejemplo 1 de spinbox").place(x=20, y=20)
Spinbox(ventana, values=("uno","dos","tres","cuatro","cinco")).place(x=20, y=50)
Label(ventana, text="Ejemplo 2 de spinbox").place(x=20, y=80)
Spinbox(ventana, from_=1,to=10, textvariable=valor).place(x=20, y=110)
Button(ventana, text="Obtener valor spinbox", command=obtener).place(x=80,y=140)
mainloop()