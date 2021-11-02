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
        buttonText = self.itemText(index)
        self.clear()
        self.addItem(buttonText)
        self.addItems(self.originalItems)

    def ItemChanged(self):
        if self.originalItems:
            return
            
        items = []
        for i in range(self.count()):
            items.append(self.itemText(i))

        self.originalItems = items
        firstButtonText = self.itemText(0)
        self.clear()
        self.addItem(firstButtonText)
        self.addItems(self.originalItems)