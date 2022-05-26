from externals.vidgear.gears import NetGear
from helpers.inputListener import Listener
import cv2
from time import perf_counter
from threading import Thread
from PyQt5.QtCore import pyqtSignal
from win32api import MapVirtualKey
from collections import deque


class Client():
    def __init__(self, win):
        self.win = win
        
        options = {
            "bidirectional_mode": True,
            }

        self.client = NetGear(
            receive_mode=True,
            address="192.168.1.132",
            port="5900",
            protocol="tcp",
            pattern=1,
            logging=False,
            **options
        )

        self.__running = True


    def start(self):
        self.__thread = Thread(target=self.__start)
        self.__thread.daemon = True
        self.__thread.start()


    def __start(self):
        #listener = Listener()
        #listener.start()

        while self.__running:
            frameStart = perf_counter()
            #instructionQueue = listener.fetch()

            data, frame = self.client.recv(return_data=[list(self.win.cmdQueue)])
            #frame = numpy.frombuffer(frame, dtype=numpy.uint8)

            #frame = frame.reshape(1200, 1600, 3)
            #print(frame.size)
            #cv2.imshow("Output Frame", frame)
            #cv2.waitKey(1)
            if frame:
                self.win.label.updated.emit(frame)

            if data is not None:
                data = deque(data)
                while data:
                    item = data.popleft()
                    if item[0] == "P":
                        ASCII = MapVirtualKey(item[1], MAPVK_VK_TO_CHAR)
                        self.win.logger.write(ch(ASCII))

                
            #halt(minFrameDelta - (frameEnd - frameStart))
            #print(1/ (frameWaitPeriodEnd - frameStart))


    def close(self):
        #listener.stop()
        self.__running = False
        self.client.close()