import cv2 
import numpy as np

#Este programa permitira dibukara objetos sobre una ventana de openCV

#Construir una imagen en blanco de un tamaño definido
imagen=255 *np.ones((400,600,3),dtype=np.uint8)

#Dibujar linea 
#Parametros de cv2.line(Superficie,coodernadainc,coordenadaFinal,color,grosor)

cv2.line(imagen,(0,0),(600,400),(255,0,0),2)

cv2.rectangle(imagen,(50,10),(200,300),(0,255,0),2)
cv2.circle(imagen,(450,100),100,(255,255,0),2)
cv2.circle(imagen,(450,100),50,(0,255,255),-1)

#Dibujar un texto
cv2.putText(imagen,'SOpenCV',(350,300),0,1,(0,0,0),2)

cv2.imshow('ss',imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()