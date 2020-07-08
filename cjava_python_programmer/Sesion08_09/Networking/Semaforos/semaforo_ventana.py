import os
from tkinter import *
from tkinter import messagebox

class SemaforoVentana:

    def __init__(self,cliente):
          # ini variables de la ventana
        self._cliente = cliente
        self._ventana = None
        self._estado_luz_roja = False 
        self._estado_luz_verde = False 
        self._btn_luz_verde = None
        self._btn_luz_roja = None
        localDirPath = os.path.dirname(os.path.abspath(__file__))
        self._ruta_imagen_verde_oscuro = localDirPath + "\\verde_oscuro.png"
        self._ruta_imagen_rojo_oscuro = localDirPath + "\\rojo_oscuro.png"
        self._ruta_imagen_verde_claro = localDirPath + "\\verde_claro.png"
        self._ruta_imagen_rojo_claro = localDirPath + "\\rojo_claro.png"
        #self._iniciar_ventana__()       
        # fin variables de la ventana

    def on_closing(self):
        # if messagebox.askokcancel("Quit", "Do you want to quit?"):
        self._ventana.destroy()
    
    def presionar_luz_verde(self):    
        photo_luz_verde = None
        
        if self._estado_luz_verde == False:            
            photo_luz_verde = PhotoImage(file=self._ruta_imagen_verde_claro)
            self._estado_luz_verde = True  # encender
        else:
            photo_luz_verde = PhotoImage(file=self._ruta_imagen_verde_oscuro)
            self._estado_luz_verde = False # apagar
        self._btn_luz_verde = Button(self._ventana, text="", command=self.presionar_luz_verde, image=photo_luz_verde)        
        self._btn_luz_verde.place(x=30,y=50)        
        mainloop()
        
    def presionar_luz_roja(self):
        photo_luz_roja = None

        if self._estado_luz_roja == False:
            photo_luz_roja = PhotoImage(file=self._ruta_imagen_rojo_claro)
            self._estado_luz_roja = True # encender
        else:
            photo_luz_roja = PhotoImage(file=self._ruta_imagen_rojo_oscuro)
            self._estado_luz_roja = False # apagar
        self._btn_luz_roja = Button(self._ventana, text="", command=self.presionar_luz_roja, image=photo_luz_roja)
        self._btn_luz_roja.place(x=190,y=50)
        mainloop()  

    def iniciar_ventana(self):        
        ventana = Tk()        
        ventana.title("Sockets ejercicio 01")
        ventana.geometry("300x180")

        Label(ventana , text=self._cliente).place(x=120, y=10)
        Label(ventana , text="Luz verde").place(x=50, y=30)
        photo_luz_verde = PhotoImage(file=self._ruta_imagen_verde_oscuro)        
        btnVerde = Button(ventana, text="", command=self.presionar_luz_verde, image=photo_luz_verde)        
        btnVerde.place(x=30,y=50)
        self._btn_luz_verde = btnVerde        
        
        Label(ventana , text="Luz roja").place(x=210, y=30)        
        photo_luz_roja = PhotoImage(file=self._ruta_imagen_rojo_oscuro)        
        btnRojo = Button(ventana, text="", command=self.presionar_luz_roja, image=photo_luz_roja)
        btnRojo.place(x=190,y=50)
        self._btn_luz_roja = btnRojo

        ventana.protocol("WM_DELETE_WINDOW", self.on_closing)
        self._ventana = ventana        
        mainloop()
