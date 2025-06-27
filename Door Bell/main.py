
import cv2
import face_recognition
import playsound
import threading
cap = cv2.VideoCapture(0)
sound_plaued = False

def ring_bell():
    playsound.playsound('doorbell-223669.mp3')
while True:
    _ , frame = cap.read()
    faces = face_recognition.face_locations(frame)
    if faces and not sound_plaued :
        threading.Thread(target=ring_bell).start()
        sound_plaued = True
    elif not faces and sound_plaued:
        sound_plaued = False
    cv2.imshow('Ai Doorbell',frame)

    if cv2.waitKey(10) ==ord('q'):
        break
