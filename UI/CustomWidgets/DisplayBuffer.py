from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QImage, QPixmap, QPainter
from PyQt5.QtCore import pyqtSignal, QPoint, Qt
from numpy import zeros, ndarray, uint8
from cv2 import cvtColor, imread, imshow, waitKey
from numba import njit


class DisplayBuffer(QLabel):
        updated = pyqtSignal(list)

        def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.setHidden(False)
                self.cursorHidden = True
                #self.resize(100, 100)
                self.blank = cvtColor(zeros((900, 1200), uint8), 8)
                self.cvVer = self.blank
                #self.updateBuffer(self.blank)

                #self.resize(100, 100)
                #print(self.width())
                #self.blank = cvtColor(zeros((self.width(), self.height()), dtype=uint8), 8)
                #self.drawBlank()

        def updateBuffer(self, frames):
                #height, width, channel = chunk.shape
                #bytesPerLine = 3 * width
                for frame in frames:
                        chunk, rect = frame
                        #fastInsert(self.cvVer, chunk, rect)
                        x, y, w, h = rect
                        self.cvVer[y:y+h, x:x+w] = chunk
                        #print("         ", w, h)

                qImg = QImage(self.cvVer.data, 1200, 900, 3*1200, QImage.Format_RGB888)
                self.setPixmap(QPixmap.fromImage(qImg))
                #self.pixmap = QPixmap.fromImage(qImg)
                #self.repaint()
                self.setCursor(Qt.BlankCursor)
                        #self.pixmap = QPixmap.fromImage(qImg)
                        #self.repaint()

                #return cpyTo


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


        def toggleCursor(self, focused):
                if focused:
                        self.setCursor(Qt.BlankCursor)

                else:
                        self.setCursor(Qt.ArrowCursor)


@njit
def fastInsert(cpyTo, chunk, rect):
        x, y, w, h = rect
        cpyTo[y:y+h, x:x+w] = chunk