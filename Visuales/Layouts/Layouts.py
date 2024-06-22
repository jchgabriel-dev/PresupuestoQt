from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout

class LayoutVSimple(QVBoxLayout):
    def __init__(self):
        super().__init__()
        self.setSpacing(0)
        self.setAlignment(Qt.AlignTop)


class LayoutVSimpleCen(QVBoxLayout):
    def __init__(self):
        super().__init__()
        self.setSpacing(0)
        self.setAlignment(Qt.AlignTop | Qt.AlignCenter)

class LayoutVCompacto(QVBoxLayout):
    def __init__(self):
        super().__init__()
        self.setContentsMargins(0,0,0,0)
        self.setSpacing(0)
        self.setAlignment(Qt.AlignTop)


class LayoutHCompacto(QHBoxLayout):
    def __init__(self):
        super().__init__()
        self.setContentsMargins(0,0,0,0)
        self.setSpacing(0)
        self.setAlignment(Qt.AlignLeft)


class LayoutHCompactoAlt(QHBoxLayout):
    def __init__(self):
        super().__init__()
        self.setContentsMargins(0,0,0,0)
        self.setSpacing(0)
        self.setAlignment(Qt.AlignRight)


class LayoutHCompactoCen(QHBoxLayout):
    def __init__(self):
        super().__init__()
        self.setContentsMargins(0,0,0,0)
        self.setSpacing(0)
        self.setAlignment(Qt.AlignCenter)

