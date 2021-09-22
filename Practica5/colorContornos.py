import cv2
import numpy as np

cap=cv2.VideoCapture(0)

#Determinar colores hsv

colorbajo=np.array([170,100,20],np.uint8)
coloralto=np.array([180,255,255],np.uint8)

while True:
    ret,frame=cap.read()
    
    if ret==True:
        framteHSV=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        fusion=cv2.inRange(framteHSV,colorbajo,coloralto)

        #Encontrar el contorno de deteccion
        contornos,_=cv2.findContours(fusion,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

        #cICLI PARA DEFINIR EL CONTORNO  y la proximidad en funcion del tamaño del objeto
        for c in contornos:
            area = cv2.contourArea(c)
            if area>1000:
                nuevoContorno=cv2.convexHull(c)#Funcion para cerrar el contorno convexo
                cv2.drawContours(frame,[c],-1,(0,255,0),5)
        cv2.imshow('Video detección Rojo',frame)

        if cv2.waitKey(1) &  0xFF==ord('s'):
            break
cap.release()
cv2.destroyAllWindows()