from PyQt5.QtWidgets import QLineEdit


class LockedLineEdit(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.text = ""
        self.textEdited.connect(self.CheckText)


    def CheckText(self):
        self.setText(self.text) #prevent the user from typing any text



class IPLineEdit(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.allowedChars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]

        self.text = ""
        self.textEdited.connect(self.CheckText)


    def CheckText(self, text):
        invalid = False
        for ch in text:
            if ch not in self.allowedChars:
                invalid = True

        if invalid:
            self.setText(self.text)

        else:
            self.text = text



class IntLineEdit(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.text = ""
        self.textEdited.connect(self.CheckText)


    def CheckText(self, text):
        if not text:
            self.text = text
            return

        try:
            int(text)
            self.text = text

        except:
            self.setText(self.text)