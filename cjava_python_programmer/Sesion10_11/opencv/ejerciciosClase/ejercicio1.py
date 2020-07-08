from cv2 import *

#Crea una ventana
namedWindow("webcam") 
#Clase para la captura de vídeo desde archivos de vídeo, 
# secuencias de imágenes o cámaras. La clase proporciona 
# C++ API para capturar vídeo desde cámaras o para leer 
# archivos de vídeo y secuencias de imágenes
vc = VideoCapture(0)  

while True:
    next, frame = vc.read()
    imshow("webcam", frame)

    #Espera una tecla pulsada.
    if waitKey(50) >= 0:
        break