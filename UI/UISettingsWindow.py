from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QRadioButton, QPushButton, QWidget
from PyQt5.QtCore import Qt
from UI.CustomWidgets.ComboBoxes import SortedComboBox
from os.path import exists, splitext, dirname, join


class UISettingsWin(QWidget):
    def __init__(self, MainWin):
        super().__init__()
        self.mainWin = MainWin
        
        self.verticalLayout = QVBoxLayout(self)

        self.horizontalLayout = QHBoxLayout()
        self.themeText = QLabel("Theme: ")
        self.themeCombo = SortedComboBox(self.mainWin.settingsDict["theme"])
        self.themeCombo.addItems(["White (default)", "Dark", "Midnight"])
        self.horizontalLayout.addWidget(self.themeText)
        self.horizontalLayout.addWidget(self.themeCombo)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.fpsRadio = QRadioButton("show stream fps")
        self.fpsRadio.setChecked(self.mainWin.settingsDict["showFps"])
        self.verticalLayout.addWidget(self.fpsRadio)

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
        selectedTheme = self.themeCombo.currentText()
        self.mainWin.ChangeTheme(selectedTheme)
        self.mainWin.settingsDict["showFps"] = self.fpsRadio.isChecked()
        self.mainWin.SaveToJson()
        self.close()