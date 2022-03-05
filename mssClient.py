from externals.vidgear.gears import ScreenGear
from externals.vidgear.gears import NetGear
import asyncio
import cv2
import profile
import pstats
import time
import numpy
from utils import *


options = {
    "bidirectional_mode": True,
    }

client = NetGear(
    receive_mode=True,
    address="192.168.1.132",
    port="5900",
    protocol="tcp",
    pattern=1,
    logging=False,
    **options
)

counter = 0
frames = 0
while True:

    frameStart = time.perf_counter()    
    frame = client.recv()
    #frame = numpy.frombuffer(frame, dtype=numpy.uint8)
    #frame = frame.reshape(1200, 1600, 3)
    #print(frame.size)
    cv2.imshow("Output Frame", frame)
        
    counter += 1
    frameEnd = time.perf_counter()
    #halt(minFrameDelta - (frameEnd - frameStart))
    frames += perf_counter() - frameStart
    #print(1/ (frameWaitPeriodEnd - frameStart))
        

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

print(1 / (frames / counter))

cv2.destroyAllWindows()
client.close()
