import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from UI.CustomWidgets.LineEdits import LockedLineEdit
from os.path import exists, splitext, dirname, join


class SaveWin(QWidget):
    def __init__(self, MainWin):
        super().__init__()
        self.LoadDefaultPath()
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
        self.dirLabel = QLabel("output file directory: ")
        self.dirLine = LockedLineEdit()
        self.browse = QPushButton("Browse...")
        self.browse.clicked.connect(self.selectDir)
        
        self.horizontalLayout.addWidget(self.dirLabel)
        self.horizontalLayout.addWidget(self.dirLine)
        self.horizontalLayout.addWidget(self.browse)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.nameLabel = QLabel("output file name: ")
        self.nameLine = QLineEdit()
        self.formatLabel = QLabel(".mp4")

        self.horizontalLayout.addWidget(self.nameLabel)
        self.horizontalLayout.addWidget(self.nameLine)
        self.horizontalLayout.addWidget(self.formatLabel)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        #add the apply button at the bottom of the window
        self.horizontalLayout = QHBoxLayout()
        self.apply = QPushButton("Apply")
        self.apply.setMaximumWidth(75)
        self.apply.clicked.connect(self.Apply)
        self.horizontalLayout.addWidget(self.apply, Qt.AlignCenter)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.setLayout(self.verticalLayout)


    #saves all of the changes
    @pyqtSlot()
    def Apply(self):
        dir = self.dirLine.text + "/"
        name = self.nameLine.text()
        ext = ".mp4"
        path = dir + name + ext

        iteration = 0
        while exists(path):
            iteration += 1
            name = name + "(" + str(iteration) + ")"
            path = dir + name + ext

        self.mainWin.outputFile = path
        self.close()


    def selectDir(self):
        location = QFileDialog.getExistingDirectory(None, "select directory", self.defaultPath, QFileDialog.ShowDirsOnly)
        if not location:
            return

        """if location[-4] != ".":
            location += ".mp4" """

        self.dirLine.text = location
        self.dirLine.setText(location)
        self.defaultPath = location
        self.MemorizePath()


    def MemorizePath(self):
        with open("lastPath.txt", 'w') as pathFile:
            pathFile.write(self.defaultPath)


    def LoadDefaultPath(self):
        with open("lastPath.txt", 'r') as pathFile:
            lastPath = pathFile.read()
            if lastPath:
                self.defaultPath = lastPath
                
            else:
                self.defaultPath = "C:\\untitled.mp4"
