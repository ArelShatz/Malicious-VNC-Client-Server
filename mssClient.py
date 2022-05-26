from externals.vidgear.gears import NetGear, WriteGear
from helpers.inputListener import Listener
import cv2
from time import perf_counter
from threading import Thread
from PyQt5.QtCore import pyqtSignal
from win32api import MapVirtualKey
from collections import deque

from socket import gethostname, gethostbyname
from numpy import ndarray
from zmq.sugar.frame import Frame

class Client():
    def __init__(self, win):
        self.win = win

        options = {
            "bidirectional_mode": True,
            "max_retries": 1
            }

        self.client = NetGear(
            receive_mode=True,
            address=gethostbyname(gethostname()),
            port="5900",
            protocol="tcp",
            pattern=1,
            logging=False,
            **options
        )

        self.writer = WriteGear(output_filename=self.win.settingsDict["outputFile"])
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
            while self.win.cmdQueue:
                self.win.cmdQueue.popleft()

            #frame = numpy.frombuffer(frame, dtype=numpy.uint8)

            #frame = frame.reshape(1200, 1600, 3)
            #print(frame.size)
            #cv2.imshow("Output Frame", frame)
            #cv2.waitKey(1)
            if frame:
                self.win.label.updated.emit(frame)
            if isinstance(rectImgs[0], Frame):
                continue

            self.win.label.updated.emit(rectImgs)
            if self.win.rec:
                self.writer.write(self.win.label.cvVer)

            if data is not None:
                data = deque(data)
                while data:
                    item = data.popleft()
                    if item[0] == "P":
                        ASCII = MapVirtualKey(item[1], MAPVK_VK_TO_CHAR)
                        self.win.logger.write(ch(ASCII))


    def close(self):
        #listener.stop()
        self.__running = False
        self.__thread.join()
        self.writer.close()
        self.client.close()