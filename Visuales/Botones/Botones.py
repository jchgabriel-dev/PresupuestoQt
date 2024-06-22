from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QPushButton, QToolButton



class BotonBar(QToolButton):
    def __init__(self, text, icon):
        super().__init__()
        self.setContentsMargins(0,0,0,0)
        self.setText(" " + text)
        self.setIcon(QIcon(f"Iconos/{icon}.png"))
        self.setIconSize(QSize(17, 17))
        self.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.setObjectName("BotonBar")


class BotonIcono(QPushButton):
    def __init__(self, icon):
        super().__init__()
        self.setContentsMargins(0,0,0,0)
        self.setIcon(QIcon(f"Iconos/{icon}.png"))
        self.setIconSize(QSize(23, 23))
        self.setFixedWidth(35)
        self.setObjectName("BotonIcono")

class BotonElementoH(QPushButton):
    def __init__(self, text, icon):
        super().__init__()
        self.setContentsMargins(0,0,0,0)
        self.setText(" " +text)
        self.setIcon(QIcon(f"Iconos/{icon}.png"))
        self.setIconSize(QSize(22, 22))
        self.setObjectName("BotonElementoH")


class BotonElementoV(QPushButton):
    def __init__(self, text, icon):
        super().__init__()
        self.setContentsMargins(0,0,0,0)
        self.setText(" " + text)
        self.setIcon(QIcon(f"Iconos/{icon}.png"))
        self.setIconSize(QSize(19, 19))
        self.setFixedHeight(23)
        self.setObjectName("BotonElementoV")


class BotonElementoVAlt(QPushButton):
    def __init__(self, text, icon):
        super().__init__()
        self.setContentsMargins(0,0,0,0)
        self.setText(" " + text)
        self.setIcon(QIcon(f"Iconos/{icon}.png"))
        self.setIconSize(QSize(19, 19))
        self.setFixedHeight(24)
        self.setObjectName("BotonElementoVAlt")


class BotonAccionMain(QPushButton):
    def __init__(self, text):
        super().__init__()
        self.setText(text)
        self.setFixedWidth(120)
        self.setObjectName("BotonAccionMain")


class BotonAccionSub(QPushButton):
    def __init__(self, text):
        super().__init__()
        self.setText(text)
        self.setFixedWidth(120)
        self.setObjectName("BotonAccionSub")


