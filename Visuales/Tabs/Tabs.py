from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTabWidget


class TabEstilizado(QTabWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("TabEstilizado")
        self.setAttribute(Qt.WA_StyledBackground, True)
