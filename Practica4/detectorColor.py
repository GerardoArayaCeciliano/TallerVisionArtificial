import cv2
import numpy as np

#Este programa dectecta solo la precencia de un color usando HSV
# Hue , Saturation and value


redBajo1=np.array([0,100,20],np.uint8)
redAlto1=np.array([10,100,20],np.uint8)

redBajo2=np.array([170,100,20],np.uint8)
redAlto2=np.array([180,255,255],np.uint8)
 

cap=cv2.VideoCapture(0)
#Crear ciclo para el gravado de video

while True:
    ret,frame= cap.read()
    if ret == True:
        #Conversion de un frma a un frameHSV
        frameHSV=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        parametro1=cv2.inRange(frameHSV,redBajo1,redAlto1)
        parametro2=cv2.inRange(frameHSV,redBajo2,redAlto2)
        fusion=cv2.add(parametro1,parametro2)
        cv2.imshow('video original',frame)
        cv2.imshow('video Convertido',fusion)
        if cv2.waitKey(40) & 0xFF==ord('s'):
            break
cap.release()
cv2.destroyAllWindows()