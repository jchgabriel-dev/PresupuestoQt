from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QTableWidget, QTableView, QAbstractItemView, QHeaderView


class TablaEstandar(QTableView):
    def __init__(self):
        super().__init__()
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setSelectionMode(QAbstractItemView.SingleSelection)
        self.verticalHeader().setDefaultSectionSize(4)
        self.verticalHeader().setVisible(False)
        self.horizontalHeader().setVisible(False)
        self.setFocusPolicy(Qt.NoFocus)
        self.horizontalHeader().setStretchLastSection(True)
        self.setObjectName("TablaEstandar")
        self.setShowGrid(False)



