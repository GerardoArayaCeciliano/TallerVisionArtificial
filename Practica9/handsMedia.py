import cv2
import mediapipe as mp

#Importamos las librerias de dibujo y deteccion esto es de lo mas importate
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    static_image_mode=False,
    max_num_hands = 1,
    min_detection_confidence=0.9) as hands:

    #Ciclo de video
    while True:
        ret, frame = cap.read()
        if ret == False:
            break
        
        #Tomamos la medida
        height, width, _ = frame.shape
        #Rotamos la imagen
        frame = cv2.flip(frame,1)
        #Transformamos de bgr a rgb
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        result = hands.process(frame_rgb)
        
        if result.multi_hand_landmarks is not None:
        #Si tenemos informacion entonces con un form recorremos los datos y dibujamos
            for hand_landmarks in result.multi_hand_landmarks:
                #Dibujar los 21 puntos de deteccion
                mp_drawing.draw_landmarks(
                frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        #Revertimos el proceso duda
        frame = cv2.flip(frame, 1)
        
        #Mostramos
        cv2.imshow("Video",frame)

        if cv2.waitKey(1) & 0xFF == ord('s'):
            break

cap.realice()
cv2.destroyAllWindows()