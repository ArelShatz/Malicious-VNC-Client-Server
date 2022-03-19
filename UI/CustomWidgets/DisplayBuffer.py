from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import pyqtSignal
from numpy import zeros, ndarray


class DisplayBuffer(QLabel):
        updated = pyqtSignal(ndarray)

        def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.setHidden(False)
                self.updateBuffer(zeros((self.width(), self.height())))


        def updateBuffer(self, frame):
                height, width = frame.shape
                bytesPerLine = 3 * width
                qImg = QImage(frame.data, width, height, bytesPerLine, QImage.Format_RGB888)
                self.setPixmap(QPixmap.fromImage(qImg))