from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QWidget
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QFont, QIcon
from UI.CustomWidgets.LineEdits import IPLineEdit


class ConnWin(QWidget):
    def __init__(self, MainWin):
        super().__init__()
        self.mainWin = MainWin

        self.verticalLayout = QVBoxLayout(self)

        self.horizontalLayout = QHBoxLayout()
        self.ipText = QLabel("enter ip: ")
        self.ipEntry = IPLineEdit()
        self.horizontalLayout.addWidget(self.ipText)
        self.horizontalLayout.addWidget(self.ipEntry)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.resText = QLabel()
        self.resText.setFont(QFont('Arial', 11))
        self.resText.setHidden(True)
        self.horizontalLayout.addWidget(self.resText)
        self.horizontalLayout.setAlignment(self.resText, Qt.AlignCenter)
        self.verticalLayout.addLayout(self.horizontalLayout)

        #add the apply button at the bottom of the window
        self.horizontalLayout = QHBoxLayout()
        self.apply = QPushButton("Connect")
        self.apply.setMaximumWidth(75)
        self.apply.clicked.connect(self.Apply)
        self.horizontalLayout.addWidget(self.apply)
        self.horizontalLayout.setAlignment(self.apply, Qt.AlignRight)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.setLayout(self.verticalLayout)
        

    #saves all of the changes
    @pyqtSlot()
    def Apply(self):
        ip = self.ipEntry.text
        valid = self.validateIP(ip)
        self.resText.setHidden(False)

        if valid:

            if ip == self.mainWin.connection:
                self.resText.setStyleSheet("color: red;")
                self.resText.setText("Already Connected To This IP")

            else:
                self.resText.setStyleSheet("color: white;")
                self.resText.setText("Connecting...")
                self.mainWin.connect(ip)
                self.close()

        else:
            self.resText.setStyleSheet("color: red;")
            self.resText.setText("Invalid IP")


    @staticmethod
    def validateIP(ip):
        components = ip.split(".")
        if len(components) != 4:
            return False

        for component in components:
            if int(component) > 255:
                return False

        return True