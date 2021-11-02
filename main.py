from PyQt5.QtWidgets import QMainWindow, QApplication, QShortcut, QMessageBox, QFileDialog
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtGui import QKeySequence, QIcon, QPalette, QColor
from main_window_ui import Ui_MainWindow
from sys import argv, exit as sysExit

from SaveWindow import SaveWin
from Palettes import *


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)  #read & load the compied .ui file
        self.closeShortcut = QShortcut(QKeySequence('Ctrl+Q'), self)
        self.closeShortcut.activated.connect(self.on_action_Exit_triggered)
        
        self.saveShortcut = QShortcut(QKeySequence('Ctrl+S'), self)
        self.saveShortcut.activated.connect(self.on_action_Save_To_triggered)
        
        self.outputFile = ""

    
    def pressedExitMsgBoxButton(self, button):
        self.msgBox.close()
        if button.text() == "&Yes":
            self.close()


    @pyqtSlot()
    def on_action_Exit_triggered(self):
        self.msgBox = QMessageBox()
        self.msgBox.setText("are you sure you want to exit?")
        self.msgBox.setWindowTitle("Quit")
        self.msgBox.setStandardButtons(QMessageBox.No | QMessageBox.Yes)
        self.msgBox.setDefaultButton(QMessageBox.No)
        self.msgBox.buttonClicked.connect(self.pressedExitMsgBoxButton)
        self.msgBox.exec_()

    @pyqtSlot()
    def on_action_Save_To_triggered(self):
        self.saveWindow = SaveWin(self)
        self.saveWindow.setWindowIcon(QIcon("Gears.png"))
        self.saveWindow.setWindowTitle("Output")
        self.saveWindow.show()
        """location = QFileDialog.getSaveFileName(self, "select file", self.defaultPath, "Video files (*.mp4)")[0]
        if not location:
            return

        if location[-4] != ".":
            location += ".mp4"

        iteration = 1
        dir = dirname(location)
        base_name, ext = splitext(location)
        while exists(location):
            newName = base_name + "(" + str(iteration) + ")"
            location = join(dir, newName, ext)
            iteration += 1

        self.currentLocation = location
        self.defaultPath = location
        self.MemorizePath()"""


if __name__ == '__main__':
    app = QApplication(argv)
    app.setStyle('Fusion')
    palette = DarkPalette()
    app.setPalette(palette)
    window = Window()
    window.setWindowIcon(QIcon("Gears.png"))
    window.setWindowTitle("Remote Desktop Software")
    window.show()
    app.exec_()
    sysExit()
