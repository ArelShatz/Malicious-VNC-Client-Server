from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import numpy


class DisplayBuffer(QLabel):
        updated = pyqtSignal(numpy.ndarray)

        def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.setHidden(False)


        def updateBuffer(self, frame):
                height, width, channel = frame.shape
                bytesPerLine = 3 * width
                qImg = QImage(frame.data, width, height, bytesPerLine, QImage.Format_RGB888)
                self.setPixmap(QPixmap.fromImage(qImg))
