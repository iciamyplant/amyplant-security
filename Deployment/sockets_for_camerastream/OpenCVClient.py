import cv2
import socket
import pickle
import os
import numpy as np

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 1000000)

server_ip = "IPserveur"#modif
server_port = xxx #modif

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

while cap.isOpened():
    ret, img = cap.read()
    cv2.imshow('Img Client', img)
    ret, buffer = cv2.imencode(".jpg", img, [int(cv2.IMWRITE_JPEG_QUALITY), 30])
    x_as_bytes = pickle.dumps(buffer)
    s.sendto((x_as_bytes),(server_ip, server_port))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()


