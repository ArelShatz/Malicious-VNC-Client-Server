# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuFIle = QtWidgets.QMenu(self.menubar)
        self.menuFIle.setObjectName("menuFIle")
        self.menuConnect = QtWidgets.QMenu(self.menubar)
        self.menuConnect.setObjectName("menuConnect")
        self.menuRecord = QtWidgets.QMenu(self.menubar)
        self.menuRecord.setObjectName("menuRecord")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_Exit = QtWidgets.QAction(MainWindow)
        self.action_Exit.setObjectName("action_Exit")
        self.action_Save_To = QtWidgets.QAction(MainWindow)
        self.action_Save_To.setObjectName("action_Save_To")
        self.action_Connect_2 = QtWidgets.QAction(MainWindow)
        self.action_Connect_2.setObjectName("action_Connect_2")
        self.action_Connect = QtWidgets.QAction(MainWindow)
        self.action_Connect.setObjectName("action_Connect")
        self.action_Security = QtWidgets.QAction(MainWindow)
        self.action_Security.setObjectName("action_Security")
        self.action_UI = QtWidgets.QAction(MainWindow)
        self.action_UI.setObjectName("action_UI")
        self.action_Start_Recording = QtWidgets.QAction(MainWindow)
        self.action_Start_Recording.setObjectName("action_Start_Recording")
        self.action_Stop_Recording = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/arel_room/Pictures/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Stop_Recording.setIcon(icon)
        self.action_Stop_Recording.setObjectName("action_Stop_Recording")
        self.menuFile.addAction(self.action_Security)
        self.menuFile.addAction(self.action_UI)
        self.menuFIle.addAction(self.action_Save_To)
        self.menuFIle.addSeparator()
        self.menuFIle.addAction(self.action_Exit)
        self.menuConnect.addAction(self.action_Connect_2)
        self.menuConnect.addAction(self.action_Connect)
        self.menuRecord.addAction(self.action_Start_Recording)
        self.menuRecord.addAction(self.action_Stop_Recording)
        self.menubar.addAction(self.menuFIle.menuAction())
        self.menubar.addAction(self.menuConnect.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuRecord.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "Settings"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuFIle.setTitle(_translate("MainWindow", "FIle"))
        self.menuConnect.setTitle(_translate("MainWindow", "Connect"))
        self.menuRecord.setTitle(_translate("MainWindow", "Record"))
        self.action_Exit.setText(_translate("MainWindow", "&Exit"))
        self.action_Save_To.setText(_translate("MainWindow", "&Save To..."))
        self.action_Connect_2.setText(_translate("MainWindow", "&Connect"))
        self.action_Connect.setText(_translate("MainWindow", "&Disconnect"))
        self.action_Security.setText(_translate("MainWindow", "&Security..."))
        self.action_UI.setText(_translate("MainWindow", "&UI..."))
        self.action_Start_Recording.setText(_translate("MainWindow", "&Start Recording"))
        self.action_Stop_Recording.setText(_translate("MainWindow", "&Stop Recording"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
