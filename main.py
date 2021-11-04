from PyQt5.QtWidgets import QMainWindow, QApplication, QShortcut, QMessageBox, QFileDialog
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtGui import QKeySequence, QIcon, QPalette, QColor
from UI.main_window_ui import Ui_MainWindow
from sys import argv, exit as sysExit

from UI.SaveWindow import SaveWin
from UI.UISettingsWindow import UISettingsWin
from UI.Palettes import WhitePalette, DarkPalette, MidnightPalette

palettes = {
        "White (default)": WhitePalette,
        "Dark": DarkPalette,
        "Midnight": MidnightPalette
    }

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, App, parent=None):
        super().__init__(parent)
        self.setupUi(self)  #read & load the compied .ui file
        self.closeShortcut = QShortcut(QKeySequence('Ctrl+Q'), self)
        self.closeShortcut.activated.connect(self.on_action_Exit_triggered)
        self.saveShortcut = QShortcut(QKeySequence('Ctrl+S'), self)
        self.saveShortcut.activated.connect(self.on_action_Save_To_triggered)
        self.app = App

        self.outputFile = ""
        self.theme = "White (default)"
        self.showFps = False

    
    def pressedExitMsgBoxButton(self, button):
        self.msgBox.close()
        if button.text() == "&Yes":
            self.close()


    def OpenWin(self, Win, name):
        self.win = Win(self)
        self.win.setWindowIcon(QIcon("Gears.png"))
        self.win.setWindowTitle(name)
        self.win.show()


    def ChangeTheme(self, paletteName):
        if self.theme != paletteName:
            paletteObj = palettes[paletteName]()
            self.theme = paletteName
            self.app.setPalette(paletteObj)


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
        self.OpenWin(SaveWin, "Select Output")


    @pyqtSlot()
    def on_action_UI_triggered(self):
        self.OpenWin(UISettingsWin, "Settings")


if __name__ == '__main__':
    app = QApplication(argv)
    app.setStyle('Fusion')
    window = Window(app)
    window.setWindowIcon(QIcon("remoteTrans.png"))
    window.setWindowTitle("Remote Desktop Software")
    window.show()
    app.exec_()
    sysExit()
