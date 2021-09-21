#Imortamos librerias
import cv2
import numpy as np
from numpy.lib.type_check import imag

#mostrar imagen original
imgOriginal=cv2.imread('chica.jpg')
cv2.imshow('Chica Original',imgOriginal)

#Matriz de datos de la imagen
brg=np.zeros((300,300,3),dtype=np.uint8)
brg[:,:,:]=(255,255,255)
cv2.imshow('BGR Estatus',brg)

#Asignar la imagen a bgr
bgr=cv2.imread('chica.jpg')
e1=bgr[:,:,0]
e2=bgr[:,:,1]
e3=bgr[:,:,2]
#Stack o conjunto de imagenes
cv2.imshow('STack en BGR',np.hstack([e1,e2,e3]))
cv2.waitKey(0)
cv2.destroyAllWindows()




