import cv2
import numpy as np

##### calculate de bounding box coordonates #####

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


faceProto="opencv_face_detector.pbtxt"
#face proto in pbtxt
faceModel="opencv_face_detector_uint8.pb"
#the face model in pb

ageProto = "age_deploy.prototxt"
ageModel = "age_net.caffemodel"

genderProto = "gender_deploy.prototxt"
genderModel = "gender_net.caffemodel"

faceNet=cv2.dnn.readNet(faceModel, faceProto)
#we need to create our model, named faceNET
#bnn = deep neural network, the latest version of opencv
ageNet=cv2.dnn.readNet(ageModel, ageProto)
gender_model=cv2.dnn.readNet(genderModel, genderProto)


MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)
ageList = ['(0-2)', '(4-6)', '(8-12)', '(15-20)', '(25-32)', '(38-43)', '(48-53)', '(60-100)']
genderList = ['Male', 'Female']



###### video capture en direct ####

video=cv2.VideoCapture(0)

while True:
    ret,frame=video.read()
    frame, bboxs=faceBox(faceNet, frame)
    #print("bboxs=", bboxs)
    for bbox in bboxs:
        face=frame[bbox[1]:bbox[3], bbox[0]:bbox[2]]
        #print(face)
        face=cv2.resize(face, (224,224))
        blob=cv2.dnn.blobFromImage(face)
        #blob=cv2.dnn.blobFromImage(face, 1.0, (224, 224), MODEL_MEAN_VALUES, swapRB=False)
        
        #---------------------------
        gender_model.setInput(blob)
        gender_class=gender_model.forward()[0]
        gender = 'Woman ' if np.argmax(gender_class) == 0 else 'Man'
        #gender=genderList[genderPred[0].argmax()]

        #---------------------------
        #ageNet.setInput(blob) 
        #agePred=ageNet.forward()
        #age=ageList[agePred[0].argmax()]

        #label="{},{}".format(gender
        cv2.putText(frame, gender, (bbox[0], bbox[1]-10), cv2.FONT_HERSHEY_PLAIN, 0.8, (255,255,255), 2)
    cv2.imshow("Age-Gender",frame)
    k=cv2.waitKey(1)
    if k==ord('q'):
        break
video.release()
cv2.destroyAllWindows()
