from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QWidget
from PyQt5.QtCore import Qt
from UI.CustomWidgets.ComboBoxes import SortedComboBox
from UI.CustomWidgets.LineEdits import IntLineEdit
from os.path import exists, splitext, dirname, join


class GeneralSettingsWin(QWidget):
    def __init__(self, MainWin):
        super().__init__()
        self.mainWin = MainWin
        
        self.verticalLayout = QVBoxLayout(self)

        self.horizontalLayout = QHBoxLayout()
        self.fpsText = QLabel("fps cap: ")
        self.fpsCombo = SortedComboBox(self.mainWin.settingsDict["fps limit"])
        self.fpsCombo.addItems(["15", "20", "24", "30", "48", "60", "unlimited"])
        self.horizontalLayout.addWidget(self.fpsText)
        self.horizontalLayout.addWidget(self.fpsCombo)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.space = QWidget()
        self.space.setMinimumWidth(10)
        self.space.setMinimumHeight(10)
        self.horizontalLayout.addWidget(self.space)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.resText = QLabel("Resolution: ")
        self.verticalLayout.addWidget(self.resText)

        self.horizontalLayout = QHBoxLayout()
        self.resWidthText = QLabel("width: ")
        self.resWidth = IntLineEdit()
        self.resWidth.setText(self.mainWin.settingsDict["resolution width"])
        self.horizontalLayout.addWidget(self.resWidthText)
        self.horizontalLayout.addWidget(self.resWidth)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.resHeightText = QLabel("height: ")
        self.resHeight = IntLineEdit()
        self.resHeight.setText(self.mainWin.settingsDict["resolution height"])
        self.horizontalLayout.addWidget(self.resHeightText)
        self.horizontalLayout.addWidget(self.resHeight)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.space = QWidget()
        self.space.setMinimumWidth(50)
        self.space.setMinimumHeight(50)
        self.horizontalLayout.addWidget(self.space)
        self.verticalLayout.addLayout(self.horizontalLayout)

        #add the apply button at the bottom of the window
        self.horizontalLayout = QHBoxLayout()
        self.apply = QPushButton("Apply")
        self.apply.setMaximumWidth(75)
        self.apply.clicked.connect(self.Apply)
        self.horizontalLayout.addWidget(self.apply, Qt.AlignCenter)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.setLayout(self.verticalLayout)


    def Apply(self):
        self.mainWin.settingsDict["fps limit"] = self.fpsCombo.currentText()
        self.mainWin.settingsDict["resolution width"] = self.resWidth.text
        self.mainWin.settingsDict["resolution height"] = self.resHeight.text
        
        self.mainWin.cmdQueue.append(("Fps Change", self.fpsCombo.currentText()))
        self.mainWin.cmdQueue.append(("Width Change", self.resWidth.text))
        self.mainWin.cmdQueue.append(("Height Change", self.resHeight.text))
        self.mainWin.SaveToJson()
        self.close()