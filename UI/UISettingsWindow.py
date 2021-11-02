import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from UI.CustomWidgets.ComboBoxes import SortedComboBox
from os.path import exists, splitext, dirname, join


class UISettingsWin(QWidget):
    def __init__(self, MainWin):
        super().__init__()
        self.currentLocation = ""
        self.mainWin = MainWin
        
        self.verticalLayout = QVBoxLayout(self)
        self.scrollArea = QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 640, 480))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.horizontalLayout = QHBoxLayout()
        self.themeText = QLabel("Theme: ")
        self.themeCombo = SortedComboBox()
        self.themeCombo.addItems(["White (default)", "Dark", "Midnight"])
        self.horizontalLayout.addWidget(self.themeText)
        self.horizontalLayout.addWidget(self.themeCombo)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.fpsRadio = QRadioButton("show stream fps")
        self.verticalLayout_2.addWidget(self.fpsRadio)

        #add the apply button at the bottom of the window
        self.horizontalLayout = QHBoxLayout()
        self.apply = QPushButton("Apply")
        self.apply.setMaximumWidth(75)
        self.apply.clicked.connect(self.Apply)
        self.horizontalLayout.addWidget(self.apply, Qt.AlignCenter)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.setLayout(self.verticalLayout)


    def Apply(self):
        selectedTheme = self.themeCombo.currentText()
        self.mainWin.ChangeTheme(selectedTheme)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = UISettingsWin()
    window.setWindowTitle("Remote Desktop Software")
    window.show()
    app.exec_()
