import cv2
import numpy as np

#Cargar el xml de haarcadcade para rostros frontales de openMaster

detectarRostro=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

########################Trabajando con una imagen ##################
#Cargamos la imagen
imagen=cv2.imread('R.jpg')
gris=cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)

##Extraemos los rostros de la imagen y damos parametros de deteccion agrupados en un arreglo
caras=detectarRostro.detectMultiScale(gris,
scaleFactor=1.3,
minNeighbors=6,
minSize=(100,100),
maxSize=(200,200))
#Desagrupar el arreglo de los rostros detectados
for(x,y,w,h) in caras:
    cv2.rectangle(imagen,(x,y),(x+w,y+h),(0,255,0),1)

cv2.imshow('Detectanto rostro',imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()

##########################Dectectando video ############################
cap=cv2.VideoCapture(0)
while True:
    ref,frame=cap.read()
   # vgris=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    v=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #DectectMultiScale en video solo 3 parametros la imagen,factor escala,cantidad de rostros factor de destresa
    vcaras= detectarRostro.detectMultiScale(v,1.1,1)
    for(x,y,w,h) in vcaras:
     cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),1)
     cv2.imshow('Detectanto rostro',frame)
     if(cv2.waitKey(1)&0xFF==ord('s')):
         break


cap.lease()
cv2.destroyAllWindows()
