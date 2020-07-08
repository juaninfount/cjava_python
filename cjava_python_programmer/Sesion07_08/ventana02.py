#Python ventana2 

from tkinter import *
'''
def imprime():
    print("Acabas de presionar el botón imprimir")
'''

ventana = Tk()
ventana.title("Segunda ventana")
botonS = Button(ventana, text="Salir",fg="red", command=ventana.quit)
botonS.pack(side=LEFT)

botonI = Button(ventana, text="Imprimir",fg="blue", command=lambda: print("Acabas de presionar el botón imprimir"))
botonI.pack(side=RIGHT)
ventana.mainloop()

