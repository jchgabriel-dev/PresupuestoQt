from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QToolBar


class ToolbarPrincipal(QToolBar):
    def __init__(self):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setObjectName("ToolbarPrincipal")


class ToolbarSub(QToolBar):
    def __init__(self):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setObjectName("ToolbarSub")
