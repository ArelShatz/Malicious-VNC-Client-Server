from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class SortedComboBox(QComboBox):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.originalItems = []
        self.activated.connect(self.ItemSelected)
        self.currentIndexChanged.connect(self.ItemChanged)

    def ItemSelected(self, index):
        self.clear()
        copy = self.originalItems.copy()
        copy.insert(0, copy.pop(index))
        self.addItems(copy)

    def ItemChanged(self):
        if not self.originalItems:
            items = []
            for i in range(self.count()):
                items.append(self.itemText(i))

            self.originalItems = items