from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class DisplayBuffer(QLabel):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.setHidden(False)
		self.pixmap = QPixmap("Gears.png")


	def updateBuffer(self, frame):
		painter = QPainter(self.pixmap)
		painter.drawPixmap(QRect(0, 0, 100, 100), self.grab())
		painter.end()
		self.pixmap.fill(Qt.black)
		self.setPixmap(self.pixmap)