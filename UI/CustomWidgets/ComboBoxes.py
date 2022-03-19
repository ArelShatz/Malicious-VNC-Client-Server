from PyQt5.QtWidgets import QComboBox


class SortedComboBox(QComboBox):
    def __init__(self, savedVal, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.saved = savedVal
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
        
        #only gets here on the initial items addition
        items = []
        for i in range(self.count()):
            items.append(self.itemText(i))

        self.originalItems = items
        firstButtonText = self.saved
        self.clear()
        self.addItem(firstButtonText)
        self.addItems(self.originalItems)