from PyQt5.QtWidgets import QWidget, QSpacerItem, QSizePolicy

from Visuales.Botones.Botones import BotonBar, BotonIcono, BotonElementoH, BotonElementoV
from Visuales.Labels.Labels import LabelTitulo
from Visuales.Layouts.Layouts import LayoutVCompacto, LayoutHCompacto
from Visuales.Toolbars.Toolbars import ToolbarPrincipal, ToolbarSub
from Visuales.Trees.Trees import ArbolCarpeta
from Visuales.Widgets.Widgets import WidgetTab, WidgetSeccion, WidgetLateralR


class Polinomica(WidgetTab):
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
        agregarCarpeta = BotonIcono("agregarCarpeta")
        editarCarpeta = BotonIcono("editarCarpeta")
        eliminarCarpeta = BotonIcono("eliminarCarpeta")
        toolbarCarpeta.addWidget(agregarCarpeta)
        toolbarCarpeta.addWidget(editarCarpeta)
        toolbarCarpeta.addWidget(eliminarCarpeta)
        treeCarpeta = ArbolCarpeta()

        widgetCarpetaMain = WidgetSeccion(200)
        layoutCarpetaMain = LayoutVCompacto()
        layoutCarpetaMain.addWidget(labelCarpeta)
        layoutCarpetaMain.addWidget(toolbarCarpeta)
        layoutCarpetaMain.addWidget(treeCarpeta)
        widgetCarpetaMain.setLayout(layoutCarpetaMain)

        # PROYECTOS

        labelProyecto = LabelTitulo("Distribucion")
        toolbarProyecto = ToolbarSub()
        agregarProyecto = BotonElementoH("Agregar", "agregarElemento")
        editarProyecto = BotonElementoH("Editar", "editarElemento")
        eliminarProyecto = BotonElementoH("Eliminar", "eliminarElemento")
        buscarProyecto = BotonElementoH("Buscar", "buscarElemento")
        asistenteProyecto = BotonElementoH("Asistente", "imprimirElemento")
        toolbarProyecto.addWidget(agregarProyecto)
        toolbarProyecto.addWidget(editarProyecto)
        toolbarProyecto.addWidget(eliminarProyecto)
        toolbarProyecto.addWidget(buscarProyecto)
        toolbarProyecto.addWidget(asistenteProyecto)

        widgetProyectoMain = WidgetSeccion()
        layoutProyectoMain = LayoutVCompacto()
        layoutProyectoMain.addWidget(labelProyecto)
        layoutProyectoMain.addWidget(toolbarProyecto)
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
        layoutSpace.addSpacing(64)
        layoutSpace.addWidget(widgetProyectoMenu)

        layoutProyectoH = LayoutHCompacto()
        layoutProyectoH.addWidget(widgetProyectoMain)
        layoutProyectoH.addLayout(layoutSpace)

        # SUBPRESUPUESTOS

        labelSubPresupuesto = LabelTitulo("Sub-presupuesto")
        toolbarSubPresupuesto = ToolbarSub()
        agregarSubPresupuesto = BotonElementoH("Agregar", "agregarElemento")
        editarSubPresupuesto= BotonElementoH("Editar", "editarElemento")
        eliminarSubPresupuesto= BotonElementoH("Eliminar", "eliminarElemento")
        toolbarSubPresupuesto.addWidget(agregarSubPresupuesto)
        toolbarSubPresupuesto.addWidget(editarSubPresupuesto)
        toolbarSubPresupuesto.addWidget(eliminarSubPresupuesto)

        widgetSubPresupuestoMain = WidgetSeccion()
        layoutSubPresupuestoMain = LayoutVCompacto()
        layoutSubPresupuestoMain.addWidget(labelSubPresupuesto)
        layoutSubPresupuestoMain.addWidget(toolbarSubPresupuesto)
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
        layoutSpaceSub.addSpacing(64)
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
