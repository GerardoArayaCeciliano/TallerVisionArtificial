import cv2
import numpy as np

#Este programa permitira dubijar objetos sobre una ventana de openCV

#Construir una imagen en blanco de tamaño definido

# imagen = 255 * np.ones((400,600,3), dtype=np.uint8)
# #parametros de line(Superficie, codenadaIni, coordenaFin,color, grosor)
# cv2.line(imagen,(0,0),(600,400),(255,0,0),2)
# cv2.line(imagen,(600,0),(0,400),(255,0,0),2)

# cv2.rectangle(imagen,(50,200),(200,300),(0,255,0),2)
# #circulo vacio
# cv2.circle(imagen,(450,100),100,(255,255,0),2)
# #circulo relleno
# cv2.circle(imagen,(450,100),50,(255,255,0),-1)

# #Texto
# cv2.putText(imagen,'OpenCV',(350,100),0,1,(0,0,0),2)

# cv2.putText(imagen,'OpenCV',(350,250),2,2,(0,0,0),2)

# cv2.imshow('MiImagen',imagen)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


cap= cv2.VideoCapture(0)

colorBajo = np.array([170,100,20], np.uint8)
colorAlto = np.array([180,255,255], np.uint8)

##############################################

#habilitamos la camara

#Crear ciclo para el gravado de video
while True:
    ret,frame = cap.read()
    #Mostrar el video en una ventana
    if ret == True:
        #Conversion frame a frameHSV
        frameHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        fusion = cv2.inRange(frameHSV,colorBajo,colorAlto)

        contornos,_ = cv2.findContours(fusion,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

        for c in contornos:
            area = cv2.contourArea(c)
            if area > 9000:
                x,y,w,h = cv2.boundingRect(c)
                cv2.putText(frame,'Elemento detectado',(x-10,y-10),0,1,(0,255,0),2)
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
              #  nuevoControno = cv2.convexHull(c)
              #  cv2.drawContours(frame, [c], -1 , (0,255,0),1)

        #Video original
        cv2.imshow('Video Original',frame)
        #Detener captura
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break

cap.release()
cv2.destroyAllWindows()