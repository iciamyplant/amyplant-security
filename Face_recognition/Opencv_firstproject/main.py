import cv2
import face_recognition
from simplefacerec import SimpleFacerec

#encode faces
sfr = SimpleFacerec()
sfr.load_encoding_images("Known_Faces/")

#cap = cv2.VideoCapture("prisonbreak_scene.avi")
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    face_locations, face_names = sfr.detect_known_faces(frame)#
    for face_loc, name in zip(face_locations, face_names):
        print(face_loc) #renvoie des int par chqe frame de la loc de la face, 4 values, top left and bottom right
        y1, x1, y2, x2 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
        cv2.putText(frame, name, (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0,0,255), 2)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 2) #displays rectangle
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)

    if key == 27: #touche esc
        break

cap.release()
cv2.destroyAllWindows() #closes video file or capturing device (webcam)
