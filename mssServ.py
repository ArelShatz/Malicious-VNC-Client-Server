"""import time
import numpy as np
import cv2
import mss.windows
from threading import Thread


mss.windows.CAPTUREBLT = 0
sct = mss.windows.MSS()
#monitor = {'top': 0, 'left': 0, 'width': 1600, 'height': 1200}
monitor = sct.monitors[1]
frameCounter = 0
frameSum = 0
iterations = 1000
minFrameDelta = 0.03333
#minFrameDelta = 0.041666
estimate = 0.01


#stops code excecution for precisely {seconds} seconds with high cpu usage
def SpinLock(seconds):
    end = 0
    start = time.perf_counter()
    while end - start < seconds:
        end = time.perf_counter()
        
    return

    #print("fps: " + str(round(1/(end - start))))


#stops code excecution for precisely {seconds} seconds with minimal cpu usage
def halt(seconds):
    while seconds > estimate:
        start = time.perf_counter()
        time.sleep(0.001)
        end = time.perf_counter()
        seconds -= (end - start)

    SpinLock(seconds)


def SendVideoStream():
    global frameSum
    for i in range(10000):
        frameStart = time.perf_counter()
        img = sct.grab(monitor)
        #cv2.imshow("stream", np.array(img))
        frameEnd = time.perf_counter()
        frameTimeElapsed = frameEnd - frameStart
        #print(abs(minFrameDelta - frameTimeElapsed))
        halt(minFrameDelta - frameTimeElapsed)
        frameWaitPeriodEnd = time.perf_counter()
        frameSum += frameWaitPeriodEnd - frameStart
        #print(frameWaitPeriodEnd - frameStart)

        print("fps: " + str(round(1/(frameWaitPeriodEnd - frameStart))))
    
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

videoThread = Thread(target=SendVideoStream)
videoThread.start()"""

"""import mss
import mss.tools


sct = mss.mss()
#sct.shot(output='fullscreenMap.bmp')
pic = sct.grab(sct.monitors[1])
part = pic.rgb[:100]
print(part)
for i in range(100):
    print(ord(part[i:i+1]))
#mss.tools.to_png(pic.rgb, pic.size, output="somePic.png")"""

"""import numpy
from mss import mss
import socket
import cv2


UDPClientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
UDPClientSock.connect(("127.0.0.1", 3389))

monitor = {'left': 0, 'top': 0, 'width': 500, 'height': 500}
with mss() as sct:
    img = sct.grab(monitor)
    rawBGR = numpy.array(img, dtype=numpy.uint8)[:, :, :3].tobytes()
    print(len(rawBGR))
    UDPClientSock.send(rawBGR[:65507])"""


from externals.vidgear.gears import ScreenGear
from externals.vidgear.gears import NetGear
from externals.vidgear.gears.helper import reducer
from PIL import Image
import profile
import pstats
import cv2
import time
import numpy

def SpinLock(seconds):
    end = 0
    start = time.perf_counter()
    while end - start < seconds:
        end = time.perf_counter()
        
    return

    #print("fps: " + str(round(1/(end - start))))


def halt(seconds):
    while seconds > estimate:
        start = time.perf_counter()
        time.sleep(0.001)
        end = time.perf_counter()
        seconds -= (end - start)

    SpinLock(seconds)


minFrameDelta = 0.016666
estimate = 0.01


options = {"jpeg_compression": True,
           "jpeg_compression_fastdct": True,
           "jpeg_compression_fastupsample": True,
           "jpeg_compression_quality": 50,
           "rle_compression": True,
           "rle_compression_strength": 6
}

server = NetGear(
    address="192.168.1.132",
    port="5900",
    protocol="tcp",
    pattern=2,
    logging=False,
    **options
)

stream = ScreenGear(backend="mss",
                    monitor=1,
                    colorspace="COLOR_BGR2RGB",
                    logging=False).start()

while True:    
    #frameStart = time.perf_counter()
        
    frame = stream.read()
    #print(frame)
    frame = numpy.flip(frame[:, :, :3], 2)
    #originalShape = originalFrame.shape
    #originalDType = originalFrame.dtype
        
    #frame = zlib.compress(originalFrame.tobytes())
    #frame = numpy.frombuffer(frame, dtype=originalDType)
    frame = reducer(frame, percentage = 30)
    server.send(frame)

    #frameEnd = time.perf_counter()
    #frameTimeElapsed = frameEnd - frameStart
    #halt(minFrameDelta - frameTimeElapsed)
    #cv2.imshow("frame", frame)
    #frameWaitPeriodEnd = time.perf_counter()
    #print(1 / (frameEnd - frameStart))


cv2.destroyAllWindows()
stream.stop()
server.close()
