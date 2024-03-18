import cv2
import socket
import pickle
import os
import numpy as np

print('coucou')
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #protocol DGRAM for udp / STREAM for TCP
ip = ""#IP adress serveur a mettre
port = #numero port a mettre
s.bind((ip, port))

while True:
    x = s.recvfrom(1000000)
    #print('coucou2')
    clientip = x[1][0]
    #print("x[1]=, x[0]=", x[1], x[0])
    data = x[0]
    data = pickle.loads(data)
    img = cv2.imdecode(data, cv2.IMREAD_COLOR)
    #print("seems to work")
    #cv2.imshow('Img Server', img)
    #if cv2.waitKey(1) & 0xFF == ord('q'):
    #    break

#cv2.destroyAllWindows()
