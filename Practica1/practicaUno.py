import cv2

#Aplicación para leer imagenes dede dispositivos
#Declarar variable asignar el contenido de una imagen mediante imread

imagen=cv2.imread('UNA.png')

#imagen en ventana el contenido de mu variable
cv2.imshow('ImagenUNA',imagen)

cv2.waitKey(0)
cv2.destroyAllWindows()

#Guardar una imagen procesada p leida en la escala de gris
imagen=cv2.imread('UNA.png',0)
cv2.imshow('ImagenUNA',imagen)
cv2.waitKey(0)
cv2.imwrite('unaGris.jpg',imagen)
cv2.destroyAllWindows()