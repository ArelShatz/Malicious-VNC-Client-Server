from collections import deque
from sys import path as sysPath
from time import sleep

from pynput.keyboard import KeyCode, Controller as keyboardController
from pynput.mouse import Button, Controller as mouseController
from threading import Thread


class Executor():
    def __init__(self):
        self.__keyboardCtrl = keyboardController()
        self.__mouseCtrl = mouseController()
        self.__running = True


    def execute(self, queue):
        if not isinstance(queue, deque):
            return
        
        self.executor = Thread(target=self.__execute, args=(queue,))
        self.executor.daemon = True
        self.executor.start()


    def __execute(self, queue):
        while queue:
            item = queue.popleft()
            cmd = item[0]
            if cmd == "M":
                self.__mouseCtrl.position = (item[1], item[2])

            elif cmd == "P":
                self.__keyboardCtrl.press(KeyCode.from_vk(item[1]))

            elif cmd == "R":
                self.__keyboardCtrl.release(KeyCode.from_vk(item[1]))

            elif cmd == "C":
                self.__mouseCtrl.position = (item[1], item[2])
                if item[4]:
                    self.__mouseCtrl.press(Button(tuple(item[3])))

                else:
                    self.__mouseCtrl.release(Button(tuple(item[3])))

            elif cmd == "S":
                self.__mouseCtrl.position = (item[1], item[2])
                self.__mouseCtrl.scroll(item[3], item[4])


    def close(self):
        self.__running = False
        self.executor.join()

        #release every button in case it was held while exiting
        self.__mouseCtrl.release(Button.left)
        self.__mouseCtrl.release(Button.right)
        self.__mouseCtrl.release(Button.middle)
        #self.__mouseCtrl.release(Button.unknown)
        self.__mouseCtrl.release(Button.x1)
        self.__mouseCtrl.release(Button.x2)
        for i in range(1, 255):
            self.__keyboardCtrl.release(KeyCode.from_vk(i))