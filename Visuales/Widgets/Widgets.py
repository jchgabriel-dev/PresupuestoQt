from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QWidget, QSizePolicy, QSpacerItem, QFrame


class WidgetTab(QWidget):
    def __init__(self):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setContentsMargins(0, 0, 0, 0)
        self.setObjectName("WidgetTab")


class WidgetSeccion(QWidget):
    def __init__(self, width=None):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setContentsMargins(0, 0, 0, 0)
        if width is not None:
            self.setFixedWidth(width)
        else:
            self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)


class WidgetSubSeccion(QWidget):
    def __init__(self, height=None):
        super().__init__()

        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setContentsMargins(0, 0, 0, 0)
        self.setObjectName("WidgetSubSeccion")
        if height is not None:
            self.setFixedHeight(height)


class WidgetLateralR(QWidget):
    def __init__(self, width=None):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setContentsMargins(0, 0, 0, 0)
        self.setObjectName("WidgetLateralR")

        if width is not None:
            self.setFixedWidth(width)


class WidgetLateralL(QWidget):
    def __init__(self, width=None):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setContentsMargins(0, 0, 0, 0)
        self.setObjectName("WidgetLateralL")

        if width is not None:
            self.setFixedWidth(width)


class WidgetSuperior(QWidget):
    def __init__(self):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setFixedHeight(23)
        self.setObjectName("WidgetSuperior")


class EspacioH(QSpacerItem):
    def __init__(self):
        super().__init__(40, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)


class LineFrame(QFrame):
    def __init__(self):
        super().__init__()
        self.setFrameShape(QFrame.HLine)
        self.setFrameShadow(QFrame.Plain)
        self.setLineWidth(1)
        self.setMidLineWidth(1)
        self.setContentsMargins(0, 0, 0, 0)
        palette = self.palette()
        palette.setColor(QPalette.WindowText, QColor("#2E3E7A"))
        self.setPalette(palette)
