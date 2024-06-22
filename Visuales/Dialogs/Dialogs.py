from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QApplication


class DialogElemento(QDialog):
    def __init__(self, text, width, height):
        super().__init__()
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self.setWindowTitle(text)
        self.setFixedSize(width, height)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setCenter()
        self.setObjectName("DialogElemento")




    def setCenter(self):
        screenGeometry = QApplication.desktop().screenGeometry()
        windowGeometry = self.frameGeometry()
        centerPoint = screenGeometry.center()
        windowGeometry.moveCenter(centerPoint)
        self.move(windowGeometry.topLeft())




