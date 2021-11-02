from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class LockedLineEdit(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.text = ""
        self.textEdited.connect(self.CheckText)

    def CheckText(self):
        self.setText(self.text) #prevent the user from typing any text
