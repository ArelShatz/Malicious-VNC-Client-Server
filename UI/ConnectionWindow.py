import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from CustomWidgets.LineEdits import LockedLineEdit


class ConnWin(QWidget):
    def __init__(self, MainWin):
        super().__init__()
        self.mainWin = MainWin

        self.verticalLayout = QVBoxLayout(self)

        self.horizontalLayout = QHBoxLayout()
        self.themeText = QLabel("Theme: ")
        self.themeCombo = SortedComboBox()
        self.themeCombo.addItems(["White (default)", "Dark", "Midnight"])
        self.horizontalLayout.addWidget(self.themeText)
        self.horizontalLayout.addWidget(self.themeCombo)
        self.verticalLayout.addLayout(self.horizontalLayout)
        


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