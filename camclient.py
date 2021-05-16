import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import socket

def recvall(client, count):
    buf = b''
    recived = 0
    while recived < count:
        newbuf = client.recv(1024)
        if not newbuf:
            return None
        buf += newbuf
        recived += len(newbuf)
    return buf

def main():
    port = 8080
    x, y = 1280, 720
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', port))
    print("connected")

    while(True):
        buffer = recvall(client, x * y * 3)
        if buffer == None:
            break
        image = np.frombuffer(buffer, dtype = "uint8").reshape(y,x,3)
        cv.imshow('img', image)
        if cv.waitKey(20) == 27:
            break

main()
