import socket
import numpy
import cv2
import time
from PIL import Image
import zlib

def halt(seconds):
    end = 0
    start = time.perf_counter()
    while end - start < seconds:
        end = time.perf_counter()
        
    return

CHUNK = 65536
UDPServerSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
UDPServerSock.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF, CHUNK)
UDPServerSock.bind(("127.0.0.1", 9999))
data = 'a'
buffer = b''

UDPServerSock.listen()

conn, addr = UDPServerSock.accept()
metaData = conn.recv(1024).decode()
#metaData = int(UDPServerSock.recvfrom(1024).decode())[0]
size, width, height = metaData.split(",")
size = int(size)


while len(buffer) < size:
    data = conn.recv(CHUNK if size - len(buffer) >= CHUNK else size - len(buffer))
    #data = UDPServerSock.recvfrom(CHUNK if length - len(buffer) >= CHUNK else length - len(buffer))[0]
    buffer += data

RGB = numpy.array(Image.frombytes("RGB", (int(width), int(height)), zlib.decompress(buffer)))
#RGB = numpy.delete(RGB[0][0], 0)
cv2.imshow("stream", RGB)
"""with open("test.txt", 'wb') as f:
    f.write(buffer)"""
    
