import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import socket




def main():
    port = 8080
    ##burde hatt socket.setsockopt greia for quick restart
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', port))
    server.listen(5)
    


    cap = cv.VideoCapture(0)
    c, addr = server.accept()
    while(True):
        print("connected to client")
        ret, frame = cap.read()
        img = np.asarray(frame)
        buffer = img.tostring()
        c.sendall(buffer)
        

        


main()


