from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtCore import Qt


#initiating a QPalette gives the default palette (system dependent)
class WhitePalette(QPalette):
	def __init__(self):
		super().__init__()


class DarkPalette(QPalette):
	def __init__(self):
		super().__init__()
		self.setColor(QPalette.Window, QColor(53, 53, 53))
		self.setColor(QPalette.WindowText, Qt.white)
		self.setColor(QPalette.Base, QColor(25, 25, 25))
		self.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
		self.setColor(QPalette.ToolTipBase, Qt.black)
		self.setColor(QPalette.ToolTipText, Qt.white)
		self.setColor(QPalette.Text, Qt.white)
		self.setColor(QPalette.Button, QColor(53, 53, 53))
		self.setColor(QPalette.ButtonText, Qt.white)
		self.setColor(QPalette.BrightText, Qt.red)
		self.setColor(QPalette.Link, QColor(42, 130, 218))
		self.setColor(QPalette.Highlight, QColor(42, 130, 218))
		self.setColor(QPalette.HighlightedText, Qt.black)


class MidNightPalette(QPalette):
	def __init__(self):
		super().__init__()
		self.setColor(QPalette.Window, QColor(53, 53, 53))
		self.setColor(QPalette.WindowText, Qt.white)
		self.setColor(QPalette.Base, QColor(25, 25, 25))
		self.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
		self.setColor(QPalette.ToolTipBase, Qt.black)
		self.setColor(QPalette.ToolTipText, Qt.white)
		self.setColor(QPalette.Text, Qt.white)
		self.setColor(QPalette.Button, QColor(53, 53, 53))
		self.setColor(QPalette.ButtonText, Qt.white)
		self.setColor(QPalette.BrightText, Qt.red)
		self.setColor(QPalette.Link, QColor(42, 130, 218))
		self.setColor(QPalette.Highlight, QColor(42, 130, 218))
		self.setColor(QPalette.HighlightedText, Qt.black)
