#Python ventana3

from tkinter import *

ventana = Tk()
ventana.title("Posicionamiento")
''' boton = Button(ventana, text="Posicionamiento diferente"   ).grid(row=0,column=1)
etiqueta = Label(ventana,text="Posicionamiento diferente"  ).grid(row=0,column=0)
etiqueta2 = Label(ventana,text="Posicionamiento diferente" ).grid(row=1,column=1)
etiqueta3 = Label(ventana,text="Posicionamiento diferente" ).grid(row=2,column=1) '''
ventana.geometry("400x200")
Label(ventana, text="Desde aquí saludamos"   ).place(x=30,y=50)
Button(ventana,text="Dame click para saludar" ,command=lambda: print("Hola a todos")).place(x=200,y=50)
Label(ventana,text="Desde aquí minimizamos" ).place(x=30,y=100)
Button(ventana,text="Dame click para minimizar",command=lambda: ventana.iconify()).place(x=200,y=100)
ventana.mainloop()

