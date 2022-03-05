import queue
import sys
import time

sys.path.append(sys.path[0] + "\\externals")    #add the externals folder to the path in order to import external dependencies
from pynput import keyboard, mouse


class Listener():
    def __init__(self):
        self.__queue = queue.Queue(maxsize=1024)
        self.__keyboardListener = keyboard.Listener(
		on_press=self.onPress,
		on_release=self.onRelease,
		win32_event_filter=self.win32_keyBlock,
                suppress=False)


        self.__mouseListener = mouse.Listener(
                on_move=self.onMove,
                on_click=self.onClick,
                on_scroll=self.onScroll,
                suppress=False)


    def start(self):
        self.__keyboardListener.start()
        self.__mouseListener.start()


    def fetch(self):
        tempQueue = self.__queue
        self.__queue = queue.Queue(maxsize=1024)
        return tempQueue


    def stop(self):
        self.__keyboardListener.stop()
        self.__mouseListener.stop()
        
        while not self.__queue.empty():
            try:
                self.__queue.get_nowait()
            except queue.Empty:
                continue
            self.__queue.task_done()
        

    #keyboard callbacks
    def onPress(self, key):
        if key == keyboard.Key.esc:
            return False

        self.__queue.put(("P", key))


    def onRelease(self, key):
        self.__queue.put(("R", key))


    def win32_keyBlock(self, msg, data):
        if data.vkCode != 0x1B:
            self.__keyboardListener._suppress = True

        else:
            self.__keyboardListener._suppress = False

        return True


    #mouse callbacks
    def onMove(self, x, y):
        self.__queue.put(("M", x, y))


    def onClick(self, x, y, button, pressed):
        self.__queue.put(("C", x, y, button, pressed))


    def onScroll(self, x, y, dx, dy):
        self.__queue.put(("S", x, y, dx, dy))
    

listener = Listener()
listener.start()
listener.stop()
