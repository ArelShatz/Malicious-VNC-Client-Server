from externals.vidgear.gears import ScreenGear
from externals.vidgear.gears import NetGear
from inputListener import Listener
import asyncio
import cv2
import time
import numpy
from utils import *



class Client():
    def __init__(self):
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

        self.__running = True


    def start(self):
        #listener = Listener()
        #listener.start()

        counter = 0
        frames = 0
        while self.__running:
            frameStart = time.perf_counter()
            #instructionQueue = listener.fetch()

            data, frame = client.recv(return_data=None)
            #frame = numpy.frombuffer(frame, dtype=numpy.uint8)

            #frame = frame.reshape(1200, 1600, 3)
            #print(frame.size)
            cv2.imshow("Output Frame", frame)
            counter += 1

            frameEnd = time.perf_counter()
            #halt(minFrameDelta - (frameEnd - frameStart))
            frames += perf_counter() - frameStart
            #print(1/ (frameWaitPeriodEnd - frameStart))

    def close(self):
        #listener.stop()
        self.__running = False
        client.close()
