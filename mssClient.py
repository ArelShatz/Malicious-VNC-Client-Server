from externals.vidgear.gears import NetGear, WriteGear
from helpers.inputListener import Listener
import cv2
from time import perf_counter
from threading import Thread
from PyQt5.QtCore import pyqtSignal
from win32api import *
from collections import deque

from socket import gethostname, gethostbyname
from numpy import ndarray
from zmq.sugar.frame import Frame

MAPVK_VK_TO_CHAR = 2

class Client():
    def __init__(self, win):
        self.win = win

        options = {
            "bidirectional_mode": True,
            "max_retries": 1
            }

        self.addr = gethostbyname(gethostname())
        self.client = NetGear(
            receive_mode=True,
            address=self.addr,
            port="5900",
            protocol="tcp",
            pattern=1,
            logging=False,
            retCh=False,
            **options
        )

        self.writer = WriteGear(output_filename=self.win.settingsDict["outputFile"], compression_mode=False)
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

            recv_data = self.client.recv(return_data=[list(self.win.cmdQueue)])
            if recv_data is None:
                continue

            data, rectImgs = recv_data
            if data is not None and self.win.keyLogger is not None:
                for item in data:
                    if item[0] == "P" and item[1] is not None:
                        #ASCII = MapVirtualKey(item[1], MAPVK_VK_TO_CHAR)
                        self.win.keyLogger.write(item[1])

            #while self.win.cmdQueue:
            #    print(self.win.cmdQueue.popleft())

            #frame = numpy.frombuffer(frame, dtype=numpy.uint8)

            #frame = frame.reshape(1200, 1600, 3)
            #print(frame.size)
            #cv2.imshow("Output Frame", frame)
            #cv2.waitKey(1)
            if isinstance(rectImgs[0], Frame):
                continue

            self.win.label.updated.emit(rectImgs)
            if self.win.rec:
                self.writer.write(self.win.label.cvVer)


    def close(self):
        #listener.stop()
        self.__running = False
        self.__thread.join()
        self.writer.close()
        self.client.close()