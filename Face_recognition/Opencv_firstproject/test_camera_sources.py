import cv2 as cv 

def testDevice(source):
   cap = cv.VideoCapture(source) 
   if cap is None or not cap.isOpened():
       print('Warning: unable to open video source: ', source)

testDevice(0) # no printout
testDevice(1) # prints message
