from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLabel


class LabelTitulo(QLabel):
    def __init__(self, text):
        super().__init__()
        self.setText(text)
        self.setObjectName("LabelTitulo")
        self.setFixedHeight(31)


class LabelSubTitulo(QLabel):
    def __init__(self, text):
        super().__init__()
        self.setText(text)
        self.setObjectName("LabelSubTitulo")
        self.setAlignment(Qt.AlignLeft)

class LabelDialog(QLabel):
    def __init__(self, text):
        super().__init__()
        self.setText(text)
        self.setObjectName("LabelDialog")
        self.setAlignment(Qt.AlignCenter)


class LabelIcono(QLabel):
    def __init__(self, icon, size):
        super().__init__()
        icono = QIcon(f"Iconos/{icon}.png")
        pixmap = icono.pixmap(size, size)
        self.setPixmap(pixmap)
        self.setAlignment(Qt.AlignCenter)


class LabelForm(QLabel):
    def __init__(self, text, width):
        super().__init__()
        self.setText(text)
        self.setFixedWidth(width)
        self.setObjectName("LabelForm")
        self.setAlignment(Qt.AlignRight)


class LabelFormSub(QLabel):
    def __init__(self, text):
        super().__init__()
        self.setText(text)
        self.setObjectName("LabelForm")
        self.setAlignment(Qt.AlignCenter)

class LabelCosto(QLabel):
    def __init__(self, text, width=None):
        super().__init__()
        self.setText(text)
        self.setObjectName("LabelCosto")
        self.setAlignment(Qt.AlignRight)

        if width is not None:
            self.setFixedWidth(width)

class LabelErrorC(QLabel):
    def __init__(self, text):
        super().__init__()
        self.setText(text)
        self.setAlignment(Qt.AlignCenter)
        self.setObjectName("LabelError")


class LabelErrorL(QLabel):
    def __init__(self, text):
        super().__init__()
        self.setText(text)
        self.setAlignment(Qt.AlignLeft)
        self.setObjectName("LabelError")


class LabelErrorForm(QLabel):
    def __init__(self, text):
        super().__init__()
        self.setText(text)
        self.setAlignment(Qt.AlignLeft)
        self.setObjectName("LabelErrorForm")


class LabelNombre(QLabel):
    def __init__(self, text):
        super().__init__()
        self.setText(text)
        self.setAlignment(Qt.AlignLeft)
        self.setObjectName("LabelNombre")

class LabelCorner(QLabel):
    def __init__(self, text):
        super().__init__()
        self.setText(text)
        self.setAlignment(Qt.AlignLeft |  Qt.AlignVCenter)
        self.setObjectName("LabelCorner")