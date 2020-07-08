from cv2 import *

#Crea una ventana
namedWindow("webcam") 
#Clase para la captura de vídeo desde archivos de vídeo, 
# secuencias de imágenes o cámaras. La clase proporciona 
# C++ API para capturar vídeo desde cámaras o para leer 
# archivos de vídeo y secuencias de imágenes
vc = VideoCapture(0)  

while True:
    #Leemos el video y capturamos frames
    next, frame = vc.read()
    #Para la conversión de color, usamos la función donde determina 
    # el tipo de conversión
    gray = cvtColor(frame, COLOR_BGR2GRAY)
    # OpenCV proporciona la función cv2.gaussianblur() para aplicar 
    # el suavizado gaussiano en la imagen de origen de entrada
    gauss = GaussianBlur(gray, (7,7), 1.5, 1.5)
    # Metodo para deteccion de bordes y asi separar objetos en una imagen
    can = Canny(gauss, 0, 30, 3)

    # Los frames procedentes del video se muestran
    imshow("webcam", can)
    # Si se presiona una tecla se cierra la venta
    if waitKey(50) >= 0:
        break