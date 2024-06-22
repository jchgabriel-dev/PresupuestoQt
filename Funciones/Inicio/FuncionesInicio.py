from PyQt5.QtCore import QObject, Qt
from PyQt5.QtGui import QIcon, QStandardItem, QStandardItemModel
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery
from PyQt5.QtWidgets import QToolButton, QComboBox

from Database.Database import DatabaseManager
from Database.Elementos.ManagerCarpeta import ManagerCarpeta
from Database.Elementos.ManagerEstado import ManagerEstado
from Database.Elementos.ManagerSubPresupuesto import ManagerSubPresupuesto
from Database.Elementos.MangerProyecto import ManagerProyecto
from Funciones.Inicio.FuncionesCarpeta import FuncionesCarpetaAgregar, FuncionesCarpetaEditar, FuncionesCarpetaEliminar
from Principal.Inicio.Carpeta import CarpetaAgregar, CarpetaEditar, CarpetaEliminar
from Principal.Inicio.Error import ErrorNormal
from Principal.Inicio.Inicio import Inicio
from Principal.Inicio.Proyecto import ProyectoAgregar, ProyectoEditar, ProyectoEliminar
from Visuales.Combos.Combos import ComboEstado


class FuncionesInicio:
    def __init__(self, main, inicio:Inicio):
        self.main = main
        self.inicio = inicio
        self.tree = self.inicio.treeCarpeta
        self.tablaProyecto = self.inicio.tablaProyecto
        self.tablaProyecto.setModel(QStandardItemModel())
        self.tablaSubPresupuesto = self.inicio.tablaSubPresupuesto
        self.tablaSubPresupuesto.setModel(QStandardItemModel())

        self.managerCarpeta = ManagerCarpeta()
        self.managerProyecto = ManagerProyecto()
        self.managerEstado = ManagerEstado()
        self.managerSubPresupuesto = ManagerSubPresupuesto()

        self.inicio.agregarProyecto.clicked.connect(lambda: self.abrirAgregarProyecto())
        self.inicio.editarProyecto.clicked.connect(lambda: self.abrirEditarProyecto())
        self.inicio.eliminarProyecto.clicked.connect(lambda: self.abrirEliminarProyecto())

        self.inicio.agregarCarpeta.clicked.connect(lambda: self.abrirAgregarCarpeta())
        self.inicio.editarCarpeta.clicked.connect(lambda: self.abrirEditarCarpeta())
        self.inicio.eliminarCarpeta.clicked.connect(lambda: self.abrirEliminarCarpeta())

        self.iniciarArbol()
        self.tablaProyecto.selectionModel().currentRowChanged.connect(self.cambiarProyecto)
        self.tablaSubPresupuesto.selectionModel().currentRowChanged.connect(self.cambiarSubPresupuesto)
        self.tree.selectionModel().selectionChanged.connect(self.restaurarIcono)
        self.setIndex()
        self.cargarArbol()



# FUNCIONES DEL ARBOL

    def setIndex(self):
        first_index = self.tree.model().index(0, 0)
        if first_index.isValid():
            self.tree.setCurrentIndex(first_index)

    def restaurarIcono(self,  selected, deselected):
        for index in selected.indexes():
            itemSelected = self.tree.model().itemFromIndex(index)
            if itemSelected is not None:
                self.main.setCarpeta(itemSelected.data(Qt.UserRole))
                self.actualizarTablaProyecto(self.main.getCarpeta())
                if not (itemSelected == self.item1 or itemSelected == self.item2):
                    itemSelected.setIcon(QIcon("Iconos/carpetaAbierta.png"))

        for index in deselected.indexes():
            item = self.tree.model().itemFromIndex(index)
            if item is not None and not (item == self.item1 or item == self.item2):
                item.setIcon(QIcon("Iconos/carpeta.png"))

    def iniciarArbol(self):
        model = QStandardItemModel()
        carpetas = self.managerCarpeta.listarCarpeta()[:2]
        primer_elemento = carpetas[0]
        icono1 = QIcon("iconos/todasCarpetas.png")
        self.item1 = QStandardItem(icono1, primer_elemento[1])
        self.item1.setData(primer_elemento[0], Qt.UserRole)
        model.appendRow(self.item1)

        segundo_elemento = carpetas[1]
        icono2 = QIcon("iconos/computadora.png")
        self.item2 = QStandardItem(icono2, segundo_elemento[1])
        self.item2.setData(segundo_elemento[0], Qt.UserRole)
        model.appendRow(self.item2)

        font = self.item1.font()
        font.setBold(True)
        self.item1.setFont(font)
        self.item2.setFont(font)
        self.tree.setModel(model)
        self.tree.setExpanded(self.tree.model().indexFromItem(self.item2), True)



    def cargarArbol(self):
        expanded_items = []
        self.recorrerArbol(self.item2, expanded_items)
        self.tree.selectionModel().selectionChanged.disconnect()
        self.item2.removeRows(0, self.item2.rowCount())
        self.tree.selectionModel().selectionChanged.connect(self.restaurarIcono)

        carpetas = self.managerCarpeta.listarCarpeta()[2:]
        id_to_item = {}

        for id_carpeta, nombre_carpeta, id_padre in carpetas:
            icono = QIcon("iconos/carpeta.png")
            item = QStandardItem(icono, nombre_carpeta)
            item.setData(id_carpeta, Qt.UserRole)
            id_to_item[id_carpeta] = item

            if id_padre == 2:
                self.item2.appendRow(item)
            else:
                parent_item = id_to_item.get(id_padre)
                if parent_item:
                    parent_item.appendRow(item)

        self.expandirArbol(self.item2, expanded_items)

    def expandirArbol(self, item, lista):

        if item.data(Qt.UserRole) in lista:
            index = self.tree.model().indexFromItem(item)
            self.tree.setExpanded(index, True)

        if item.data(Qt.UserRole) == self.main.getCarpeta():
            index = self.tree.model().indexFromItem(item)
            self.tree.setCurrentIndex(index)

        for row in range(item.rowCount()):
            child_item = item.child(row)
            self.expandirArbol(child_item, lista)

    def recorrerArbol(self, item, expanded_items):
        if item is None:
            return

        if self.tree.isExpanded(self.tree.model().indexFromItem(item)):
            expanded_items.append(item.data(Qt.UserRole))

        for row in range(item.rowCount()):
            child_item = item.child(row)
            self.recorrerArbol(child_item, expanded_items)

    def setIdCarpeta(self, id):
        self.main.setCarpeta(id)


# FUNCIONES DE LA TABLA PROYECTOS

    def cambiarProyecto(self, index):
        model = self.tablaProyecto.model()
        id = model.index(index.row(), 1).data(Qt.UserRole)
        self.main.setProyecto(id)
        self.actualizarTablaSubPresupuesto()

    def actualizarTablaProyecto(self, id):
        model = self.tablaProyecto.model()
        model.clear()
        if id == 1:
            proyectos = self.managerProyecto.listarProyecto()
        else:
            proyectos = self.managerProyecto.listarProyectoCarpeta(id)


        for estado, id, nombre in proyectos:
            itemEstado = QStandardItem()
            itemId = QStandardItem(str(id).zfill(4))
            itemId.setData(id, Qt.UserRole)
            itemNombre = QStandardItem(QIcon("iconos/proyecto.png"), nombre)

            model.appendRow([itemEstado, itemId, itemNombre])
            combo = self.getEstadoCombo(estado)
            self.tablaProyecto.setIndexWidget(itemEstado.index(), combo)

        if proyectos:
            first_index = self.tablaProyecto.model().index(0, 0)
            if first_index.isValid():
                self.tablaProyecto.setCurrentIndex(first_index)

        self.tablaProyecto.setColumnWidth(0, 20)
        self.tablaProyecto.setColumnWidth(1, 60)

    def getEstadoCombo(self, estado):
        combo = ComboEstado()
        estados = self.managerEstado.listarEstado()
        iconos = ["estadoVacio", "estadoAprobado", "estadoBloqueado", "estadoCancelado", "estadoCritico", "estadoUrgente", "estadoCambios"]

        for id, nombre in estados:
            combo.addItem(QIcon(f"Iconos/{iconos[id-1]}.png"), "", id)

        combo.setCurrentIndex(combo.findData(estado))
        combo.currentIndexChanged.connect(self.cambiarEstado)
        return combo

    def cambiarEstado(self, index):
        self.managerProyecto.editarProyectoEstado(index+1, self.main.getProyecto())



# FUNCIONES DE LA TABLA SUB-PRESUPUESTOS

    def cambiarSubPresupuesto(self, index):
        model = self.tablaSubPresupuesto.model()
        id = model.index(index.row(), 1).data(Qt.UserRole)
        self.main.setSubPresupuesto(id)

    def actualizarTablaSubPresupuesto(self):
        model = self.tablaSubPresupuesto.model()
        model.clear()
        subPresupuestos = self.managerSubPresupuesto.listarSubPresupuestoProyecto(self.main.getProyecto())

        for id, orden, nombre in subPresupuestos:
            itemEspacio = QStandardItem()
            itemOrden = QStandardItem(str(orden).zfill(4))
            itemOrden.setData(id, Qt.UserRole)
            itemNombre = QStandardItem(QIcon("Iconos/subPresupuesto.png"), nombre)

            model.appendRow([itemEspacio, itemOrden, itemNombre])

        self.tablaSubPresupuesto.setColumnWidth(0, 20)
        self.tablaSubPresupuesto.setColumnWidth(1, 60)

        if subPresupuestos:
            first_index = self.tablaSubPresupuesto.model().index(0, 0)
            if first_index.isValid():
                self.tablaSubPresupuesto.setCurrentIndex(first_index)






# ABRIR VENTANAS RELACIONADAS CON CARPETAS

    def abrirAgregarCarpeta(self):
        if self.main.getCarpeta() == 1:
            ventana_error = ErrorNormal("No se puede agregar sub-carpetas a esta carpeta")
            self.main.oscurecerVentana(ventana_error)

        else:
            ventana = CarpetaAgregar()
            FuncionesCarpetaAgregar(ventana, self.main.getCarpeta(), self)
            self.main.oscurecerVentana(ventana)

    def abrirEditarCarpeta(self):
        if self.main.getCarpeta() == 1 or self.main.getCarpeta() == 2:
            ventana_error = ErrorNormal("No se puede modificar el nombre de esta carpeta")
            self.main.oscurecerVentana(ventana_error)

        else:
            ventana = CarpetaEditar()
            FuncionesCarpetaEditar(ventana, self.main.getCarpeta(), self)
            self.main.oscurecerVentana(ventana)

    def abrirEliminarCarpeta(self):
        if self.main.getCarpeta() == 1 or self.main.getCarpeta() == 2:
            ventana_error = ErrorNormal("No se puede eliminar esta carpeta")
            self.main.oscurecerVentana(ventana_error)

        else:
            ventana = CarpetaEliminar()
            FuncionesCarpetaEliminar(ventana, self.main.getCarpeta(), self)
            self.main.oscurecerVentana(ventana)


# ABRIR VENTANAS RELACIONADAS CON PROYECTOS

    def abrirAgregarProyecto(self):
        ventana = ProyectoAgregar()
        self.main.oscurecerVentana(ventana)

    def abrirEditarProyecto(self):
        ventana = ProyectoEditar()
        self.main.oscurecerVentana(ventana)

    def abrirEliminarProyecto(self):
        ventana = ProyectoEliminar()
        self.main.oscurecerVentana(ventana)

