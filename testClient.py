import socket
import mss
import numpy
import time
import cv2
import zlib

def halt(seconds):
    end = 0
    start = time.perf_counter()
    while end - start < seconds:
        end = time.perf_counter()
        
    return

CHUNK = 65536
UDPClientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
UDPClientSock.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF, CHUNK)
UDPClientSock.connect(("127.0.0.1", 9999))
done = False
iteration = 1

sct = mss.mss()
mainMonitor = sct.monitors[1]
img = sct.grab(mainMonitor)
buffer = zlib.compress(img.rgb)

shape = (str(mainMonitor["width"]) + "," + str(mainMonitor["height"])).encode()
size = (str(len(buffer)) + ",").encode()

#UDPClientSock.sendto(size + shape, ("127.0.0.1", 9999))
UDPClientSock.send(size + shape)
s = time.perf_counter()
while buffer != b'':
    iteration += 1
    #UDPClientSock.sendto(buffer[:CHUNK - 29], ("127.0.0.1", 9999))
    #buffer = buffer[CHUNK-29:]
    UDPClientSock.send(buffer[:CHUNK])
    buffer = buffer[CHUNK:]

e = time.perf_counter()
print(e - s)
print(iteration)
#print(img.rgb[-1000:])
"""input()
with open("test.txt", "rb") as f:
    text = f.read()

if text == img.rgb:
    print("yes")"""
