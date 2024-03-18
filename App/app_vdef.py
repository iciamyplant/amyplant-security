from flask import Flask,render_template,Response
import cv2
import numpy as np

app=Flask(__name__)


##### func faceBox : calculate de bounding box coordonates #####

def faceBox(faceNet, frame):
    frameHeight=frame.shape[0]
    frameWidth=frame.shape[1]
    blob=cv2.dnn.blobFromImage(frame, 1.0, (300,300), [104,117,123], swapRB=False)
    faceNet.setInput(blob)
    detection=faceNet.forward()
    bboxs=[]
    for i in range(detection.shape[2]):
        confidence=detection[0,0,i,2]
        if confidence>0.7:
            x1=int(detection[0,0,i,3]*frameWidth)
            y1=int(detection[0,0,i,4]*frameHeight)
            x2=int(detection[0,0,i,5]*frameWidth)
            y2=int(detection[0,0,i,6]*frameHeight)
            bboxs.append([x1,y1,x2,y2])
            cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 1)
    return frame, bboxs


##### load models files and create faceNet, age_model, genderModel #####
faceProto="opencv_face_detector.pbtxt"
faceModel="opencv_face_detector_uint8.pb"

ageProto = "age_deploy.prototxt"
ageModel = "age_net.caffemodel"

genderProto = "gender_deploy.prototxt"
genderModel = "gender_net.caffemodel"

faceNet=cv2.dnn.readNet(faceModel, faceProto)
age_model=cv2.dnn.readNet(ageModel, ageProto)
gender_model=cv2.dnn.readNet(genderModel, genderProto)


def generate_frames():
    output_indexes = np.array([i for i in range(0, 101)])
    camera=cv2.VideoCapture(0)
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 1020)

    while True:
        ## read the camera frame
        ret,img=camera.read()            
        frame, bboxs=faceBox(faceNet, img)
        
        if not ret:
            print("no camera found")
            break
        else:
            for bbox in bboxs:
                face=frame[bbox[1]:bbox[3], bbox[0]:bbox[2]]
                face=cv2.resize(face, (224,224))
                blob=cv2.dnn.blobFromImage(face)

                #---------------------------
                gender_model.setInput(blob)
                gender_class=gender_model.forward()[0]
                gender = 'Woman ' if np.argmax(gender_class) == 0 else 'Man'
                #---------------------------
                age_model.setInput(blob)
                age_dist = age_model.forward()[0]
                age = round(np.sum(age_dist * output_indexes), 2)

                label="{},{}".format(gender, age)
                cv2.putText(frame, label, (bbox[0], bbox[1]-10), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (0,255,0), 1)
            ret,buffer=cv2.imencode('.jpg',frame)
            frame=buffer.tobytes()
        yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__=="__main__":
    app.run(debug=True)

