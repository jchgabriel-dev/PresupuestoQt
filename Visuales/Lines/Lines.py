from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLineEdit, QCheckBox, QCalendarWidget, QDateTimeEdit, QSpinBox, QComboBox


class LineElemento(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setObjectName("LineElemento")

class LineForm(QLineEdit):
    def __init__(self, width):
        super().__init__()
        self.setFixedWidth(width)
        self.setObjectName("LineForm")

class LineFormIcon(QLineEdit):
    def __init__(self, width, icon):
        super().__init__()
        self.setFixedWidth(width)
        self.setObjectName("LineFormIcon")
        mainIcon = QIcon(f"Iconos/{icon}.png")
        self.addAction(mainIcon, QLineEdit.ActionPosition.TrailingPosition)

class CheckForm(QCheckBox):
    def __init__(self, text):
        super().__init__()
        self.setText(text)
        self.setObjectName("CheckForm")


class TimeForm(QDateTimeEdit):
    def __init__(self, width):
        super().__init__()
        self.setCalendarPopup(True)
        self.setCalendarWidget(CalendarForm())
        self.setFixedWidth(width)
        self.setDate(QDate.currentDate())
        self.setObjectName("TimeForm")
        self.setDisplayFormat("dd / MM / yyyy")


class CalendarForm(QCalendarWidget):
    def __init__(self):
        super().__init__()
        self.setFixedWidth(350)
        self.setObjectName("CalendarForm")