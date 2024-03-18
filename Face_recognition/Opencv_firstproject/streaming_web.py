from flask import Flask
from flask import render_template
from flask import Response
import cv2
import face_recognition
from simplefacerec import SimpleFacerec

app = Flask(__name__) #init the app

#encode faces
sfr = SimpleFacerec()
sfr.load_encoding_images("Known_Faces/")

#cap = cv2.VideoCapture("prisonbreak_scene.avi")
cap = cv2.VideoCapture(0)

def generate():
    while True:
        ret, frame = cap.read()
        if ret:
            face_locations, face_names = sfr.detect_known_faces(frame)#
            for face_loc, name in zip(face_locations, face_names):
                #print(face_loc) #renvoie des int par chqe frame de la loc de la face, 4 values, top left and bottom right
                y1, x1, y2, x2 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
                cv2.putText(frame, name, (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0,0,255), 2)
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 2) #displays rectangle
                (flag, encodedImage) = cv2.imencode(".jpg", frame) 
                if not flag:
                    continue
                yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encodedImage) + b'\r\n')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/video_feed")
def video_feed():
    return Response(generate(),
                    mimetype = "multipart/x-mixed-replace; boundary=frame")

if __name__ == "__main__":
    app.run(debug=True)

cap.release()
