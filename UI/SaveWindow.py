import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from UI.CustomWidgets.LineEdits import LockedLineEdit
from os.path import exists, splitext, dirname, join, basename


class SaveWin(QWidget):
    def __init__(self, MainWin):
        super().__init__()
        self.LoadDefaultPath()
        self.currentLocation = ""
        self.mainWin = MainWin
        
        self.verticalLayout = QVBoxLayout(self)     
        
        self.horizontalLayout = QHBoxLayout()
        self.dirLabel = QLabel("output file directory: ")
        self.dirLine = LockedLineEdit()
        self.dirLine.setText(DirOf(self.mainWin.outputFile))
        self.browse = QPushButton("Browse...")
        self.browse.clicked.connect(self.selectDir)
        
        self.horizontalLayout.addWidget(self.dirLabel)
        self.horizontalLayout.addWidget(self.dirLine)
        self.horizontalLayout.addWidget(self.browse)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.nameLabel = QLabel("output file name: ")
        self.nameLine = QLineEdit()
        self.nameLine.setText(basename(self.mainWin.outputFile).split('.')[0])
        self.formatLabel = QLabel(".mp4")

        self.horizontalLayout.addWidget(self.nameLabel)
        self.horizontalLayout.addWidget(self.nameLine)
        self.horizontalLayout.addWidget(self.formatLabel)
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
        self.horizontalLayout.addWidget(self.apply)
        self.horizontalLayout.setAlignment(self.apply, Qt.AlignRight)
        self.verticalLayout.addLayout(self.horizontalLayout)
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



def DirOf(Path):
    Reversed = Path[::-1]
    index = len(Reversed) - Reversed.find("/") - 1
    return Path[:index]
