from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QColor
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlQueryModel, QSqlQuery
from PyQt5.QtWidgets import QTreeView, QFrame, QStyledItemDelegate, QAbstractItemView


class ArbolCarpeta(QTreeView):
    def __init__(self):
        super().__init__()

        self.setHeaderHidden(True)
        self.setObjectName("ArbolCarpeta")
        self.setFrameShape(QFrame.StyledPanel)
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setFocusPolicy(Qt.NoFocus)
        self.setSelectionMode(QAbstractItemView.SingleSelection)


