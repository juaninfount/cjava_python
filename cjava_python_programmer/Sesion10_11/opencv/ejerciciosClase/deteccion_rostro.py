#Ejemplo de deteccion facial con OpenCV y Python
#Por Glare
#www.robologs.net
  
import numpy as np
import cv2
  
#Cargamos la plantilla e inicializamos la webcam:
# !!! RECUERDA CAMBIAR EL PATH DEL ARCHIVO .xml POR EL TUYO!!!
face_cascade = cv2.CascadeClassifier('C:/Users/JORGE CORDOVA/Desktop/CJAVA\OPENCV/archivosxml/haarcascade_frontalface_alt.xml')
cap = cv2.VideoCapture(0)
  
while(True):
    #Leemos un frame y lo guardamos
    valido, img = cap.read()
 
    #Si el frame se ha capturado correctamente, continuamos
    if valido:
  
        #Convertimos la imagen a blanco y negro
        img_gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
      
        # Buscamos las coordenadas de los rostros (si los hay) y
        # guardamos su posicion
        array_rostros = face_cascade.detectMultiScale(img_gris, 1.3, 5)
      
        # Iteramos el array de rostros y pintamos un recuadro alrededor de
        # cada uno
        for (x,y,w,h) in array_rostros:
                cv2.rectangle(img,(x,y),(x+w,y+h),(125,255,0),2)
      
        #Mostramos la imagen
        cv2.imshow('img',img)
          
        #Con la tecla 'q' salimos del programa
        if cv2.waitKey(1) & 0xFF == ord('q'):
                break
cap.release()
cv2.destroyAllWindows()