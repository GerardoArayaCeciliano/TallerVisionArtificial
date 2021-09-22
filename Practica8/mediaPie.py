import cv2
import mediapipe as mp

#iniciar camara de video
cap = cv2.VideoCapture(0)

#importamos liberias de dibujo y deteccion de rostros
mp_face_mesh = mp.solutions.face_mesh
mp_drawing=mp.solutions.drawing_utils

#iniciamos el ciclo y ponemos parametros a la variable face_mesh
with mp_face_mesh.FaceMesh(
    static_image_mode=False,
    max_num_faces=1,
    min_detection_confidence=0.5) as face_mesh:
    while True:
        ref,frame=cap.read()
        if ref==False:
            break
        #Obtener el alto y el ancho del video
        h,w,_=frame.shape
        #Convertimos la imagen digital de BGR A RGB
        frame_rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

        result=face_mesh.process(frame_rgb)

        if result.multi_face_landmarks is not None:
            for face_lankmark in result.multi_face_landmarks:
                mp_drawing.draw_landmarks(
                    frame,face_lankmark,mp_face_mesh.FACE_CONNECTIONS,
                    #Dibulo los puntos de la cara
                    mp_drawing.DrawingSpec(color=(0,255,255),thickness=1,circle_radius=1),
                    #Dibuja las lineas de union
                    mp_drawing.DrawingSpec(color=(255,0,255),thickness=1))
        
        cv2.imshow('Rostro detectado',frame)

        if(cv2.waitKey(1) & 0xFF==ord('S')):
            break
cap.realice()
cv2.destroyAllWindows()