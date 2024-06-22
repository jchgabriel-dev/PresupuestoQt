import sys

from PyQt5.QtCore import QFile, QTextStream, Qt
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QApplication, QComboBox, QHBoxLayout

from Database.Database import DatabaseManager
from Database.Elementos.ManagerCarpeta import ManagerCarpeta
from Principal.Inicio.Carpeta import CarpetaAgregar, CarpetaEditar, CarpetaEliminar
from Principal.Inicio.Error import ErrorNormal
from Principal.Inicio.Inicio import Inicio
from Principal.Inicio.Proyecto import ProyectoAgregar, ProyectoEditar, ProyectoEliminar
from Principal.Polinomica.Polinomica import Polinomica
from Principal.Presupuesto.Presupuesto import Presupuesto
from Principal.Programacion.Programacion import Programacion
from Visuales.Combos.Combos import ComboPresupuesto
from Visuales.Labels.Labels import LabelNombre, LabelCorner
from Visuales.Layouts.Layouts import LayoutVCompacto, LayoutHCompactoCen, LayoutHCompacto
from Visuales.Tabs.Tabs import TabEstilizado
from Funciones.Inicio.FuncionesInicio import FuncionesInicio
from Visuales.Widgets.Widgets import WidgetSuperior, WidgetSeccion


class MainWindow(QMainWindow):
    def __init__(self):
        self.idProyecto = -1
        self.idSubPresupuesto = -1
        self.idCarpeta = -1

        super().__init__()
        db = DatabaseManager()
        db.create_database()
        self.setAttribute(Qt.WA_StyledBackground, True)

        self.setWindowTitle("Presupuesto")
        self.setGeometry(100, 100, 800, 600)
        self.cargarCss(self,  "Tablas", "Combos", "Lines", "Dialogs","Trees", "Botones", "Widgets", "Toolbars" , "Tabs", "Labels")

        mainLayout = LayoutVCompacto()
        mainWidget = QWidget()
        mainWidget.setLayout(mainLayout)

        cornerWidget = WidgetSeccion()
        cornerLayout = LayoutHCompacto()
        cornerNombre = LabelCorner("Sub-presupuesto : ")
        cornerCombo = ComboPresupuesto()
        cornerCombo.addItems(["INSTALACIONES ELECTRICAS 1", "INSTALACIONES ELECTRICAS 2", "INSTALACIONES ELECTRICAS 3"])
        cornerLayout.addWidget(cornerNombre)
        cornerLayout.addWidget(cornerCombo)
        cornerWidget.setLayout(cornerLayout)

        self.tabPrincipal = TabEstilizado()
        self.tabInicio = Inicio()
        FuncionesInicio(self, self.tabInicio)

        tab2 = Presupuesto()
        tab3 = Polinomica()
        tab4 = Programacion()

        self.tabPrincipal.setCornerWidget(cornerWidget, Qt.TopRightCorner)
        self.tabPrincipal.addTab(tab2, "Presupuesto")

        self.tabPrincipal.addTab(self.tabInicio , "Inicio")
        self.tabPrincipal.addTab(tab3, "F. Polinomica")
        self.tabPrincipal.addTab(tab4, "Programacion")

        barraSuperior = WidgetSuperior()
        barraNombre = LabelNombre("PROYECTO DE EJEMPLO")
        barraLayout = LayoutHCompactoCen()
        barraLayout.addWidget(barraNombre)
        barraSuperior.setLayout(barraLayout)

        mainLayout.addWidget(barraSuperior)
        mainLayout.addWidget(self.tabPrincipal)
        self.setCentralWidget(mainWidget)

    def setCarpeta(self, id):
        self.idCarpeta = id
        print(self.idCarpeta)

    def setProyecto(self, id):
        self.idProyecto = id
        print(self.idProyecto)

    def setSubPresupuesto(self, id):
        self.idSubPresupuesto = id
        print(self.idSubPresupuesto)

    def getCarpeta(self):
        return self.idCarpeta

    def getProyecto(self):
        return self.idProyecto

    def getSubPresupuesto(self):
        return self.idSubPresupuesto

    def oscurecerVentana(self, dialog):
        overlay = QWidget(self)
        overlay.setStyleSheet("background-color: rgba(0, 0, 0, 100);")
        overlay.setGeometry(0, 0, self.width(), self.height())
        overlay.show()
        self.cargarCss(dialog, "Tablas", "Combos", "Lines", "Dialogs","Trees", "Botones", "Widgets", "Toolbars" , "Tabs", "Labels")
        dialog.exec_()
        overlay.deleteLater()

    def cargarCss(self, main, *css_files):
        combined_style_sheet = ""
        for file in css_files:
            path = f"Visuales/{file}/{file}.css"
            css = QFile(path)
            if css.open(QFile.ReadOnly | QFile.Text):
                stream = QTextStream(css)
                style_sheet = stream.readAll()
                combined_style_sheet += style_sheet

        main.setStyleSheet(combined_style_sheet)



def cargarCss(main, *css_files):
    combined_style_sheet = ""
    for file in css_files:
        path = f"Visuales/{file}/{file}.css"
        css = QFile(path)
        if css.open(QFile.ReadOnly | QFile.Text):
            stream = QTextStream(css)
            style_sheet = stream.readAll()
            combined_style_sheet += style_sheet

    main.setStyleSheet(combined_style_sheet)

if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    #temporal = ErrorNormal("1212")
    #cargarCss(temporal, "Tablas", "Combos", "Lines", "Dialogs", "Trees", "Botones", "Widgets", "Toolbars", "Tabs", "Labels")
    #temporal.show()

    sys.exit(app.exec_())

