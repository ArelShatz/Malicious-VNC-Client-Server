from sys import argv, exit as sysExit, path as sysPath
sysPath.append(sysPath[0] + "\\externals")    #add the externals folder to the path in order to import external dependencies

from PyQt5.QtWidgets import QMainWindow, QApplication, QShortcut, QMessageBox, QFileDialog, QPushButton
from PyQt5.QtCore import Qt, pyqtSlot, QState
from PyQt5.QtGui import QKeySequence, QIcon, QPalette, QColor, QImage
from UI.main_window_ui import Ui_MainWindow
from json import load, dump, decoder

from UI.SaveWindow import SaveWin
from UI.ConnectionWindow import ConnWin
from UI.UISettingsWindow import UISettingsWin
from UI.Palettes import WhitePalette, DarkPalette, MidnightPalette

from mssServ import Server
from mssClient import Client


palettes = {
        "White (default)": WhitePalette,
        "Dark": DarkPalette,
        "Midnight": MidnightPalette
    }


defaultSettings = {
                "outputFile": "",
                "theme": "White (default)",
                "showFps": False
            }


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, App, parent=None):
        super().__init__(parent)
        self.setupUi(self)  #read & load the compiled .ui file

        self.addAction(self.action_Save_To)
        self.addAction(self.action_UI)
        self.addAction(self.action_Exit)
        self.addAction(self.action_Fullscreen)
        self.addAction(self.action_Connect)
        self.addAction(self.action_Disconnect)
        self.addAction(self.action_Bind)
        self.addAction(self.action_Close)


        self.fullscreenExitShortcut = QShortcut('ESC', self)
        self.fullscreenExitShortcut.activated.connect(lambda: self.ToggleFullscreen(self.windowState() & 11))   #change 3rd bit (fullscreen flag) to 0 (XXXX & 1011(11) = X0XX)

        self.app = App
        self.app.aboutToQuit.connect(self.closeEvent)

        self.settingsDict = self.ReadFromJson()     #load the saved settings
        tempTheme = self.settingsDict["theme"]
        self.settingsDict["theme"] = "White (default)"
        self.ChangeTheme(tempTheme)

        self.label.updated.connect(self.label.updateBuffer)

        self.bind = False
        self.connection = ""


    def ToggleFullscreen(self, newState):
        self.setWindowState(newState);
        self.menubar.setHidden(newState)


    def OpenWin(self, Win, name):
        self.win = Win(self)
        self.win.setAttribute(Qt.WA_DeleteOnClose)
        self.win.setWindowIcon(QIcon("Gears.png"))
        self.win.setWindowTitle(name)
        self.win.show()


    def ChangeTheme(self, paletteName):
        if self.settingsDict["theme"] != paletteName:
            paletteObj = palettes[paletteName]()
            self.settingsDict["theme"] = paletteName
            self.app.setPalette(paletteObj)


    def SaveToJson(self):
        conf = open('config.json', 'w')
        dump(self.settingsDict, conf, indent=0)
        conf.close()


    def ReadFromJson(self):
        try:
            conf = open('config.json', 'r')
            settings = load(conf)
            conf.close()

        except (FileNotFoundError, decoder.JSONDecodeError):   #if config file does not exists/is empty/is corrupted, create a default save file and load the default settings
            conf = open('config.json', 'w')
            dump(defaultSettings, conf, indent=0)
            conf.close()
            settings = defaultSettings

        finally:
            return settings


    def connect(self, ip):
        self.connection = ip
        self.server = Server(self.connection)
        self.server.start()


    def closeEvent(self, event):
        self.msgBox = QMessageBox()
        self.msgBox.setAttribute(Qt.WA_DeleteOnClose)
        self.msgBox.setText("are you sure you want to exit?")
        self.msgBox.setWindowIcon(QIcon("Gears.png"))
        self.msgBox.setWindowTitle("Quit")
        self.msgBox.setStandardButtons(QMessageBox.No | QMessageBox.Yes)
        self.msgBox.setDefaultButton(QMessageBox.No)
        reply = self.msgBox.exec_()

        if reply == QMessageBox.Yes:
            self.on_action_Disconnect_triggered()
            self.on_action_Close_triggered()
            event.accept()

        else:
            event.ignore()


    @pyqtSlot()
    def on_action_Exit_triggered(self):
        self.close()    #fire the close event


    @pyqtSlot()
    def on_action_Save_To_triggered(self):
        self.OpenWin(SaveWin, "Select Output")


    @pyqtSlot()
    def on_action_UI_triggered(self):
        self.OpenWin(UISettingsWin, "Settings")


    @pyqtSlot()
    def on_action_Fullscreen_triggered(self):
        self.ToggleFullscreen(self.windowState() ^ Qt.WindowFullScreen)


    @pyqtSlot()
    def on_action_Connect_triggered(self):
        self.OpenWin(ConnWin, "Connection Manager")


    @pyqtSlot()
    def on_action_Disconnect_triggered(self):
        if self.connection:
            self.connection = ""
            self.server.close()


    @pyqtSlot()
    def on_action_Bind_triggered(self):
        self.bind = True
        self.client = Client(self)
        self.client.start()


    @pyqtSlot()
    def on_action_Close_triggered(self):
        if self.bind:
            self.bind = False
            self.client.close()
            self.label.updateBuffer(self.label.blank)


if __name__ == '__main__':
    app = QApplication(argv)
    app.setStyle('Fusion')
    window = Window(app)
    window.setAttribute(Qt.WA_DeleteOnClose)
    window.setWindowIcon(QIcon("remoteTrans.png"))
    window.setWindowTitle("Remote Desktop Software")
    window.show()
    app.exec_()
    print('\n'.join(repr(w) for w in app.allWidgets()))
    sysExit()