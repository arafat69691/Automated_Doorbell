import cv2
import face_recognition
cap = cv2.VideoCapture(0)
while True:
    _ , frame = cap.read()
    faces = face_recognition.face_locations(frame)
    print(faces)
    cv2.imshow('Ai Doorbell',frame)

    if cv2.waitKey(10) ==ord('q'):
        break

