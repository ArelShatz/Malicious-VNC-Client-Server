from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QImage, QPixmap, QPainter
from PyQt5.QtCore import pyqtSignal, QPoint, Qt
from numpy import zeros, ndarray, uint8
from cv2 import cvtColor, imread


class DisplayBuffer(QLabel):
        updated = pyqtSignal(ndarray)

        def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.setHidden(False)
                #self.resize(100, 100)
                self.blank = cvtColor(zeros((100, 100), dtype=uint8), 8)
                #self.updateBuffer(self.blank)


        def updateBuffer(self, frame):
                height, width, channel = frame.shape
                bytesPerLine = 3 * width
                qImg = QImage(frame.data, width, height, bytesPerLine, QImage.Format_RGB888)
                self.setPixmap(QPixmap.fromImage(qImg))
                #self.pixmap = QPixmap.fromImage(qImg)
                #self.repaint()


        """def paintEvent(self, event):
	        size = self.size()
	        painter = QPainter(self)
	        point = QPoint(0,0)
	        scaledPix = self.pixmap.scaled(size, Qt.KeepAspectRatio, transformMode = Qt.SmoothTransformation)
	        # start painting the label from left upper corner
	        point.setX((size.width() - scaledPix.width())/2)
	        point.setY((size.height() - scaledPix.height())/2)
	        print (point.x(), ' ', point.y())
	        painter.drawPixmap(point, scaledPix)"""


        def drawBlank(self):
        		self.updateBuffer(self.blank)