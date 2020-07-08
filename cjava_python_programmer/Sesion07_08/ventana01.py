#python
from tkinter import *
import time

def parpadear():
    ventana.iconify()
    time.sleep(3)
    ventana.deiconify()

ventana = Tk()    
ventana.title("Primer ventana en tkinter")
boton = Button(ventana, text="Evento", command=parpadear)
boton.pack()
ventana.mainloop()