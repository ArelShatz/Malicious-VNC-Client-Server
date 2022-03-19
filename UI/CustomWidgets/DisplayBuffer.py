from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import pyqtSignal
from numpy import zeros, ndarray, uint8
from cv2 import cvtColor


class DisplayBuffer(QLabel):
        updated = pyqtSignal(ndarray)

        def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.setHidden(False)
                self.blank = cvtColor(zeros((self.width(), self.height()), dtype=uint8), 8)
                self.updateBuffer(self.blank)


        def updateBuffer(self, frame):
                height, width, channel = frame.shape
                bytesPerLine = 3 * width
                qImg = QImage(frame.data, width, height, bytesPerLine, QImage.Format_RGB888)
                self.setPixmap(QPixmap.fromImage(qImg))