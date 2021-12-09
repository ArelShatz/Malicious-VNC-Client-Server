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
UDPServerSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
UDPServerSock.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF, CHUNK)
UDPServerSock.bind(("127.0.0.1", 9999))
data = 'a'
buffer = b''

#UDPServerSock.listen()

#conn, addr = UDPServerSock.accept()
#length = int(conn.recv(8).decode())
length = int(UDPServerSock.recvfrom(8).decode())[0]
print(length)

while len(buffer) < length:
    #data = conn.recv(CHUNK)
    data = UDPServerSock.recvfrom(CHUNK if length - len(buffer) >= CHUNK else length - len(buffer))[0]
    buffer += data
    print(len(buffer))

RGB = numpy.array(Image.frombytes("RGB", (1600, 1200), zlib.decompress(buffer)))
#RGB = numpy.delete(RGB[0][0], 0)
cv2.imshow("stream", RGB)
"""with open("test.txt", 'wb') as f:
    f.write(buffer)"""
    
