from PyQt5.QtCore import Qt, QSize, QRect
from PyQt5.QtGui import QColor, QPalette, QIcon
from PyQt5.QtWidgets import QComboBox, QStyledItemDelegate, QStyle, QFrame


class ComboForm(QComboBox):
    def __init__(self, width):
        super().__init__()
        self.setFixedWidth(width)
        self.setObjectName("ComboForm")

class ComboPresupuesto(QComboBox):
    def __init__(self):
        super().__init__()
        self.setFixedWidth(280)
        self.setFixedHeight(25)
        self.setObjectName("ComboPresupuesto")
        self.setItemDelegate(ComboPresupuestoDelegado(self))

class ComboPresupuestoDelegado(QStyledItemDelegate):
    def paint(self, painter, option, index):
        painter.save()

        selected_background_color = QColor("#3956C0")
        selected_text_color = QColor("#ffffff")

        if option.state & QStyle.State_Selected:
            painter.fillRect(option.rect, selected_background_color)
            painter.setPen(selected_text_color)
        else:
            painter.setPen(option.palette.color(QPalette.Text))

        text = index.data()
        padding = option.rect.adjusted(10, 0, 0, 0)
        painter.drawText(padding, Qt.AlignVCenter, text)
        painter.restore()

    def sizeHint(self, option, index):
        return QSize(option.rect.width(), 23)


class ComboEstado (QComboBox):
    def __init__(self):
        super().__init__()
        self.setContentsMargins(0,0,0,0)
        self.setFixedWidth(36)
        self.setObjectName("ComboEstado")
        self.setItemDelegate(ComboEstadoDelegado(self))

    def wheelEvent(self, event):
        event.ignore()


class ComboEstadoDelegado(QStyledItemDelegate):
    def paint(self, painter, option, index):
        painter.save()

        selected_background_color = QColor("#3956C0")
        selected_text_color = QColor("#ffffff")

        if option.state & QStyle.State_Selected:
            painter.fillRect(option.rect, selected_background_color)
            painter.setPen(selected_text_color)
        else:
            painter.setPen(option.palette.color(QPalette.Text))

        icon = index.data(Qt.DecorationRole)
        icon_rect = QRect(option.rect.left() + 10, option.rect.top()+2, 16, 16)

        if isinstance(icon, QIcon):
            icon.paint(painter, icon_rect, Qt.AlignVCenter)

        painter.restore()

    def sizeHint(self, option, index):
        return QSize(option.rect.width(), 21)


