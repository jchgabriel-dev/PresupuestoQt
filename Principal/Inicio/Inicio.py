from PyQt5.QtWidgets import QWidget, QSpacerItem, QSizePolicy

from Principal.Inicio.Proyecto import ProyectoAgregar
from Visuales.Botones.Botones import BotonBar, BotonIcono, BotonElementoH, BotonElementoV
from Visuales.Labels.Labels import LabelTitulo, LabelForm, LabelCosto
from Visuales.Layouts.Layouts import LayoutVCompacto, LayoutHCompacto, LayoutHCompactoAlt
from Visuales.Lines.Lines import LineForm
from Visuales.Tablas.Tablas import TablaEstandar
from Visuales.Toolbars.Toolbars import ToolbarPrincipal, ToolbarSub
from Visuales.Trees.Trees import ArbolCarpeta
from Visuales.Widgets.Widgets import WidgetTab, WidgetSeccion, WidgetLateralR, WidgetSubSeccion


class Inicio(WidgetTab):
    def __init__(self):
        super().__init__()

        # TOOLBAR

        toolbar = ToolbarPrincipal()
        base = BotonBar("Base de datos", "base")
        importar = BotonBar("Importar", "importar")
        exportar = BotonBar("Exportar", "exportar")
        toolbar.addWidget(base)
        toolbar.addWidget(importar)
        toolbar.addWidget(exportar)

        # CARPETAS

        labelCarpeta = LabelTitulo("Distribucion")
        toolbarCarpeta  = ToolbarSub()
        self.agregarCarpeta = BotonIcono("agregarCarpeta")
        self.editarCarpeta = BotonIcono("editarCarpeta")
        self.eliminarCarpeta = BotonIcono("eliminarCarpeta")
        toolbarCarpeta.addWidget(self.agregarCarpeta)
        toolbarCarpeta.addWidget(self.editarCarpeta)
        toolbarCarpeta.addWidget(self.eliminarCarpeta)
        self.treeCarpeta = ArbolCarpeta()

        widgetCarpetaMain = WidgetSeccion(200)
        layoutCarpetaMain = LayoutVCompacto()
        layoutCarpetaMain.addWidget(labelCarpeta)
        layoutCarpetaMain.addWidget(toolbarCarpeta)
        layoutCarpetaMain.addWidget(self.treeCarpeta)
        widgetCarpetaMain.setLayout(layoutCarpetaMain)

        # PROYECTOS

        labelProyecto = LabelTitulo("Proyectos")
        toolbarProyecto = ToolbarSub()
        self.agregarProyecto = BotonElementoH("Agregar", "agregarElemento")
        self.editarProyecto = BotonElementoH("Editar", "editarElemento")
        self.eliminarProyecto = BotonElementoH("Eliminar", "eliminarElemento")
        buscarProyecto = BotonElementoH("Buscar", "buscarElemento")
        asistenteProyecto = BotonElementoH("Asistente", "imprimirElemento")
        toolbarProyecto.addWidget(self.agregarProyecto)
        toolbarProyecto.addWidget(self.editarProyecto)
        toolbarProyecto.addWidget(self.eliminarProyecto)
        toolbarProyecto.addWidget(buscarProyecto)
        toolbarProyecto.addWidget(asistenteProyecto)
        self.tablaProyecto = TablaEstandar()
        costoWidget = WidgetSubSeccion(55)
        costoLayout = LayoutVCompacto()

        labelCostoDirecto = LabelCosto("Costo directo")
        labelCostoDirectoV = LabelCosto("-", 120)
        layoutCostoDirecto = LayoutHCompactoAlt()
        layoutCostoDirecto.addWidget(labelCostoDirecto)
        layoutCostoDirecto.addWidget(labelCostoDirectoV)

        labelCostoIndirecto = LabelCosto("Costo indirecto")
        labelCostoIndirectoV = LabelCosto("-", 120)
        layoutCostoIndirecto = LayoutHCompactoAlt()
        layoutCostoIndirecto.addWidget(labelCostoIndirecto)
        layoutCostoIndirecto.addWidget(labelCostoIndirectoV)

        labelCostoTotal = LabelCosto("Costo total")
        labelCostoTotalV = LabelCosto("-", 120)
        layoutCostoTotal  = LayoutHCompactoAlt()
        layoutCostoTotal.addWidget(labelCostoTotal)
        layoutCostoTotal.addWidget(labelCostoTotalV)

        costoLayout.addSpacing(3)
        costoLayout.addLayout(layoutCostoDirecto)
        costoLayout.addSpacing(3)
        costoLayout.addLayout(layoutCostoIndirecto)
        costoLayout.addSpacing(3)
        costoLayout.addLayout(layoutCostoTotal)
        costoWidget.setLayout(costoLayout)


        widgetProyectoMain = WidgetSeccion()
        layoutProyectoMain = LayoutVCompacto()
        layoutProyectoMain.addWidget(labelProyecto)
        layoutProyectoMain.addWidget(toolbarProyecto)
        layoutProyectoMain.addWidget(self.tablaProyecto)
        layoutProyectoMain.addWidget(costoWidget)
        widgetProyectoMain.setLayout(layoutProyectoMain)


        widgetProyectoMenu = WidgetLateralR(120)
        layoutProyectoMenu = LayoutVCompacto()
        copiarProyecto = BotonElementoV("Copiar", "copiar")
        cortarProyecto = BotonElementoV("Cortar", "cortar")
        pegarProyecto = BotonElementoV("Pegar", "pegar")
        layoutProyectoMenu.addSpacing(10)
        layoutProyectoMenu.addWidget(copiarProyecto)
        layoutProyectoMenu.addWidget(cortarProyecto)
        layoutProyectoMenu.addWidget(pegarProyecto)
        layoutProyectoMenu.addSpacing(30)
        widgetProyectoMenu.setLayout(layoutProyectoMenu)

        layoutSpace = LayoutVCompacto()
        layoutSpace.addSpacing(30)
        layoutSpace.addWidget(widgetProyectoMenu)

        layoutProyectoH = LayoutHCompacto()
        layoutProyectoH.addWidget(widgetProyectoMain)
        layoutProyectoH.addLayout(layoutSpace)

        # SUBPRESUPUESTOS

        labelSubPresupuesto = LabelTitulo("Sub-presupuestos")
        toolbarSubPresupuesto = ToolbarSub()
        self.agregarSubPresupuesto = BotonElementoH("Agregar", "agregarElemento")
        self.editarSubPresupuesto= BotonElementoH("Editar", "editarElemento")
        self.eliminarSubPresupuesto= BotonElementoH("Eliminar", "eliminarElemento")
        toolbarSubPresupuesto.addWidget(self.agregarSubPresupuesto)
        toolbarSubPresupuesto.addWidget(self.editarSubPresupuesto)
        toolbarSubPresupuesto.addWidget(self.eliminarSubPresupuesto)
        self.tablaSubPresupuesto = TablaEstandar()

        widgetSubPresupuestoMain = WidgetSeccion()
        widgetSubPresupuestoMain.setMaximumHeight(250)
        layoutSubPresupuestoMain = LayoutVCompacto()
        layoutSubPresupuestoMain.addWidget(labelSubPresupuesto)
        layoutSubPresupuestoMain.addWidget(toolbarSubPresupuesto)
        layoutSubPresupuestoMain.addWidget(self.tablaSubPresupuesto)
        widgetSubPresupuestoMain.setLayout(layoutSubPresupuestoMain)

        widgetSubPresupuestoMenu = WidgetLateralR(120)
        layoutSubPresupuestoMenu = LayoutVCompacto()
        subirSubPresupuesto = BotonElementoV("Arriba", "arriba")
        bajarSubPresupuesto = BotonElementoV("Abajo", "abajo")
        copiarSubPresupuesto = BotonElementoV("Copiar", "copiar")
        pegarSubPresupuesto = BotonElementoV("Pegar", "pegar")
        layoutSubPresupuestoMenu.addSpacing(10)
        layoutSubPresupuestoMenu.addWidget(subirSubPresupuesto)
        layoutSubPresupuestoMenu.addWidget(bajarSubPresupuesto)
        layoutSubPresupuestoMenu.addWidget(copiarSubPresupuesto)
        layoutSubPresupuestoMenu.addWidget(pegarSubPresupuesto)
        layoutSubPresupuestoMenu.addSpacing(30)
        widgetSubPresupuestoMenu.setLayout(layoutSubPresupuestoMenu)

        layoutSpaceSub = LayoutVCompacto()
        layoutSpaceSub.addSpacing(30)
        layoutSpaceSub.addWidget(widgetSubPresupuestoMenu)

        layoutSubProyectoH = LayoutHCompacto()
        layoutSubProyectoH.addWidget(widgetSubPresupuestoMain)
        layoutSubProyectoH.addLayout(layoutSpaceSub)

        # SUBPRINCIPAL

        layoutInicio = LayoutHCompacto()
        layoutInicio.addSpacing(10)
        layoutInicio.addWidget(widgetCarpetaMain)
        layoutInicio.addSpacing(10)
        layoutVInicio = LayoutVCompacto()
        layoutVInicio.addLayout(layoutProyectoH)
        layoutVInicio.addSpacing(10)
        layoutVInicio.addLayout(layoutSubProyectoH)
        layoutInicio.addLayout(layoutVInicio)
        layoutInicio.addSpacing(10)

        # PRINCIPAL

        mainLayout = LayoutVCompacto()
        mainLayout.addWidget(toolbar)
        mainLayout.addSpacing(10)
        mainLayout.addLayout(layoutInicio)
        mainLayout.addSpacing(10)

        self.setLayout(mainLayout)

