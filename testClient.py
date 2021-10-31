import socket
import mss
import numpy
import time
import cv2

def halt(seconds):
    end = 0
    start = time.perf_counter()
    while end - start < seconds:
        end = time.perf_counter()
        
    return

UDPClientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
UDPClientSock.connect(("127.0.0.1", 3389))
CHUNK = 2048
done = False
iteration = 1

sct = mss.mss()
img = sct.grab(sct.monitors[1])
buffer = img.rgb

#print(str(len(img.rgb)).encode())
UDPClientSock.send(str(len(img.rgb)).encode())
s = time.time()
while buffer != b'':
    UDPClientSock.sendto(buffer[:CHUNK], ("127.0.0.1", 3389))
    buffer = buffer[CHUNK:]

e = time.time()
print(e - s)
print(img.rgb[-1000:])
"""input()
with open("test.txt", "rb") as f:
    text = f.read()

if text == img.rgb:
    print("yes")"""
