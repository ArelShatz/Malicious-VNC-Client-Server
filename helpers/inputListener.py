from collections import deque
from sys import path as sysPath

from pynput.keyboard import Key, Listener as keyboardListener
from pynput.mouse import Button, Listener as mouseListener


class Listener():
    def __init__(self, grabKeyInput=False, grabMouseInput=False, blockInput=False, return_char=False):
        self.grabKeyInput = grabKeyInput
        self.grabMouseInput = grabMouseInput
        self.blockInput = blockInput
        self.return_char = return_char

        self.__queue = deque(maxlen=1024)
        self.keyboardListener = keyboardListener(
		on_press=self.onPress,
		on_release=self.onRelease,
		win32_event_filter=self.win32_keyBlock,
                suppress=False)


        self.mouseListener = mouseListener(
                on_move=self.onMove,
                on_click=self.onClick,
                on_scroll=self.onScroll,
                win32_event_filter=self.win32_mouseBlock,
                suppress=False)


    def start(self):
        self.keyboardListener.start()
        self.mouseListener.start()


    def fetch(self):
        tempQueue = self.__queue
        self.__queue = deque(maxlen=1024)
        return list(tempQueue)


    def stop(self):
        self.keyboardListener.stop()
        self.mouseListener.stop()
        
        while len(self.__queue) != 0:
            self.__queue.popleft()


    #keyboard callbacks
    def onPress(self, key):
        if not self.grabKeyInput:
            return

        if len(self.__queue) != self.__queue.maxlen:
            if self.return_char:
                if isinstance(key, Key):
                    self.__queue.append(("P", key.value.char))
                else:
                    self.__queue.append(("P", key.char))

            else:
                if isinstance(key, Key):
                    self.__queue.append(("P", key.value.vk))
                else:
                    self.__queue.append(("P", key.vk))


    def onRelease(self, key):
        if not self.grabKeyInput:
            return

        if len(self.__queue) != self.__queue.maxlen:
            if self.return_char:
                if isinstance(key, Key):
                    self.__queue.append(("R", key.value.char))
                else:
                    self.__queue.append(("R", key.char))

            else:
                if isinstance(key, Key):
                    self.__queue.append(("R", key.value.vk))
                else:
                    self.__queue.append(("R", key.vk))


    def win32_keyBlock(self, msg, data):
        if self.blockInput:
            self.keyboardListener._suppress = True

        else:
            self.keyboardListener._suppress = False

        return True


    #mouse callbacks
    def onMove(self, x, y):
        if not self.grabMouseInput:
            return

        if len(self.__queue) != self.__queue.maxlen:
            self.__queue.append(("M", x, y))


    def onClick(self, x, y, button, pressed):
        if not self.grabMouseInput:
            return

        if len(self.__queue) != self.__queue.maxlen:
            self.__queue.append(("C", x, y, button.value, pressed))


    def onScroll(self, x, y, dx, dy):
        if not self.grabMouseInput:
            return

        if len(self.__queue) != self.__queue.maxlen:
            self.__queue.append(("S", x, y, dx, dy))


    def win32_mouseBlock(self, msg, data):
        if self.blockInput:
            self.mouseListener._suppress = True

        else:
            self.mouseListener._suppress = False

        return True