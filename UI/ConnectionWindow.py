import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from CustomWidgets.LineEdits import LockedLineEdit


class ConnWin(QWidget):
    def __init__(self):
        super().__init__()

        self.verticalLayout = QVBoxLayout(self)
        self.scrollArea = QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 380, 280))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        


if __name__ == '__main__':
    app = QApplication([])
    window = ConnWin()
    window.setWindowIcon(QIcon("Gears.png"))
    window.setWindowTitle("output")
    window.show()
    app.exec_()

    app1 = QApplication([])
    app1.setStyle('Windows')
    window = ConnWin()
    window.setWindowIcon(QIcon("Gears.png"))
    window.setWindowTitle("output")
    window.show()
    app1.exec_()