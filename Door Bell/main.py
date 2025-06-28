


import cv2
import face_recognition
import threading
import pygame


pygame.mixer.init()
pygame.mixer.music.load("doorbell-223669.mp3")  

cap = cv2.VideoCapture(0)
sound_played = False

def ring_bell():
    pygame.mixer.music.play()

while True:
    _, frame = cap.read()
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    faces = face_recognition.face_locations(rgb_frame)

    if faces and not sound_played:
        threading.Thread(target=ring_bell).start()
        sound_played = True
    elif not faces and sound_played:
        sound_played = False

    cv2.imshow('AI Doorbell', frame)

    if cv2.waitKey(10) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

