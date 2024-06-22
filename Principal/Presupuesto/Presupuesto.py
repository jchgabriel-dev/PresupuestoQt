from PyQt5.QtWidgets import QWidget, QSpacerItem, QSizePolicy

from Visuales.Botones.Botones import BotonBar, BotonIcono, BotonElementoH, BotonElementoV, BotonElementoVAlt
from Visuales.Labels.Labels import LabelTitulo
from Visuales.Layouts.Layouts import LayoutVCompacto, LayoutHCompacto
from Visuales.Toolbars.Toolbars import ToolbarPrincipal, ToolbarSub
from Visuales.Trees.Trees import ArbolCarpeta
from Visuales.Widgets.Widgets import WidgetTab, WidgetSeccion, WidgetLateralR, WidgetLateralL


class Presupuesto(WidgetTab):
    def __init__(self):
        super().__init__()


        # TOOLBAR

        toolbar = ToolbarPrincipal()
        self.asistente = BotonBar("Asistente", "asistente")
        self.imprimir = BotonBar("Imprimir", "imprimir")
        self.excel = BotonBar("Excel", "excel")
        self.recalcular = BotonBar("Recalcular", "recalcular")
        self.insumos = BotonBar("Insumos", "insumos")
        self.pie = BotonBar("Pie de presupuesto", "presupuesto")
        self.ver = BotonBar("Ver", "ver")
        self.plantilla = BotonBar("Planilla", "planilla")
        self.metrados = BotonBar("Metrados", "metrado")
        self.especificaciones = BotonBar("Especificaciones", "especificaciones")


        toolbar.addWidget(self.asistente)
        toolbar.addWidget(self.imprimir)
        toolbar.addWidget(self.excel)
        toolbar.addWidget(self.recalcular)
        toolbar.addWidget(self.insumos)
        toolbar.addWidget(self.pie)
        toolbar.addWidget(self.ver)
        toolbar.addWidget(self.plantilla)
        toolbar.addWidget(self.metrados)
        toolbar.addWidget(self.especificaciones)

        # PRESUPUESTO

        labelPresupuesto = LabelTitulo("Presupuesto")
        widgetPresupuestoMain = WidgetSeccion()
        layoutPresupuestoMain = LayoutVCompacto()
        layoutPresupuestoMain.addWidget(labelPresupuesto)
        widgetPresupuestoMain.setLayout(layoutPresupuestoMain)


        widgetPresupuestoAciones = WidgetLateralR(130)
        layoutPresupuestoAciones = LayoutVCompacto()
        subirPresupuesto = BotonElementoV("Subir todo", "subirTodo")
        subirParcialPresupuesto = BotonElementoV("Subir item", "subirParcial")
        bajarParcialPresupuesto = BotonElementoV("Bajar item", "bajarParcial")
        bajarPresupuesto = BotonElementoV("Bajar todo", "bajarTodo")
        copiarPresupuesto = BotonElementoV("Copiar", "copiar")
        cortarPresupuesto = BotonElementoV("Cortar", "cortar")
        pegarPresupuesto = BotonElementoV("Pegar", "pegar")
        layoutPresupuestoAciones.addSpacing(10)
        layoutPresupuestoAciones.addWidget(subirPresupuesto)
        layoutPresupuestoAciones.addWidget(subirParcialPresupuesto)
        layoutPresupuestoAciones.addWidget(bajarParcialPresupuesto)
        layoutPresupuestoAciones.addWidget(bajarPresupuesto)
        layoutPresupuestoAciones.addSpacing(10)
        layoutPresupuestoAciones.addWidget(copiarPresupuesto)
        layoutPresupuestoAciones.addWidget(cortarPresupuesto)
        layoutPresupuestoAciones.addWidget(pegarPresupuesto)
        layoutPresupuestoAciones.addSpacing(10)
        widgetPresupuestoAciones.setLayout(layoutPresupuestoAciones)
        layoutSpaceR = LayoutVCompacto()
        layoutSpaceR.addSpacing(33)
        layoutSpaceR.addWidget(widgetPresupuestoAciones)

        widgetPresupuestoMenu = WidgetLateralL(130)
        layoutPresupuestoMenu = LayoutVCompacto()
        partida = BotonElementoVAlt("Insertar partida", "partida")
        titulo = BotonElementoVAlt("Insertar titulo", "titulo")
        subTitulo = BotonElementoVAlt("Insertar subtitulo", "subtitulo")
        tabulacion = BotonElementoVAlt("Tabulacion", "tabulacionInversa")
        tabulacionInv = BotonElementoVAlt("Tabulacion Inv.", "tabulacion")
        quitar = BotonElementoVAlt("Quitar", "quitar")
        vincular = BotonElementoVAlt("Vincular analisis", "vincular")
        layoutPresupuestoMenu.addSpacing(5)
        layoutPresupuestoMenu.addWidget(partida)
        layoutPresupuestoMenu.addWidget(titulo)
        layoutPresupuestoMenu.addWidget(subTitulo)
        layoutPresupuestoMenu.addWidget(tabulacion)
        layoutPresupuestoMenu.addWidget(tabulacionInv)
        layoutPresupuestoMenu.addWidget(quitar)
        layoutPresupuestoMenu.addWidget(vincular)
        layoutPresupuestoMenu.addSpacing(5)
        widgetPresupuestoMenu.setLayout(layoutPresupuestoMenu)
        layoutSpaceL = LayoutVCompacto()
        layoutSpaceL.addSpacing(33)
        layoutSpaceL.addWidget(widgetPresupuestoMenu)

        layoutPresupuestoH = LayoutHCompacto()
        layoutPresupuestoH.addSpacing(10)
        layoutPresupuestoH.addLayout(layoutSpaceL)
        layoutPresupuestoH.addWidget(widgetPresupuestoMain)
        layoutPresupuestoH.addLayout(layoutSpaceR)
        layoutPresupuestoH.addSpacing(10)

        # SUBPRESUPUESTOS

        labelAnalisis = LabelTitulo("Analisis de costos")
        widgetAnalisisMain = WidgetSeccion()
        layoutAnalisisMain = LayoutVCompacto()
        layoutAnalisisMain.addWidget(labelAnalisis)
        widgetAnalisisMain.setLayout(layoutAnalisisMain)

        widgetAnalisisResumen = WidgetLateralR(120)
        layoutAnalisisResumen = LayoutVCompacto()
        subirSubPresupuesto = BotonElementoV("Arriba", "arriba")
        bajarSubPresupuesto = BotonElementoV("Abajo", "abajo")
        copiarSubPresupuesto = BotonElementoV("Copiar", "copiar")
        pegarSubPresupuesto = BotonElementoV("Pegar", "pegar")
        layoutAnalisisResumen.addSpacing(10)
        layoutAnalisisResumen.addWidget(subirSubPresupuesto)
        layoutAnalisisResumen.addWidget(bajarSubPresupuesto)
        layoutAnalisisResumen.addWidget(copiarSubPresupuesto)
        layoutAnalisisResumen.addWidget(pegarSubPresupuesto)
        layoutAnalisisResumen.addSpacing(30)
        widgetAnalisisResumen.setLayout(layoutAnalisisResumen)
        layoutSpaceRA = LayoutVCompacto()
        layoutSpaceRA.addSpacing(64)
        layoutSpaceRA.addWidget(widgetAnalisisResumen)

        widgetAnalisisMenu = WidgetLateralL(130)
        layoutAnalisisMenu = LayoutVCompacto()
        insertarInsumos = BotonElementoVAlt("Insertar insumo", "todasCarpetas")
        subPartida = BotonElementoVAlt("Ins. subpartida", "subpartida")
        buscarPrecio = BotonElementoVAlt("Buscar Precio", "buscar")
        quitarAnalisis = BotonElementoVAlt("Quitar", "quitarAnalisis")
        importarOtro = BotonElementoVAlt("Importar de otro", "importarOtro")
        editarInsumo = BotonElementoVAlt("Editar Insumo", "editarInsumo")
        importarPrecios = BotonElementoVAlt("Importar precios", "importarPrecio")
        layoutAnalisisMenu.addSpacing(5)
        layoutAnalisisMenu.addWidget(insertarInsumos)
        layoutAnalisisMenu.addWidget(subPartida)
        layoutAnalisisMenu.addWidget(buscarPrecio)
        layoutAnalisisMenu.addWidget(quitarAnalisis)
        layoutAnalisisMenu.addWidget(importarOtro)
        layoutAnalisisMenu.addWidget(editarInsumo)
        layoutAnalisisMenu.addWidget(importarPrecios)

        layoutAnalisisMenu.addSpacing(5)
        widgetAnalisisMenu.setLayout(layoutAnalisisMenu)
        layoutSpaceLM = LayoutVCompacto()
        layoutSpaceLM.addSpacing(33)
        layoutSpaceLM.addWidget(widgetAnalisisMenu)
        layoutAnalisisH = LayoutHCompacto()
        layoutAnalisisH.addSpacing(10)
        layoutAnalisisH.addLayout(layoutSpaceLM)
        layoutAnalisisH.addWidget(widgetAnalisisMain)
        layoutAnalisisH.addLayout(layoutSpaceRA)
        layoutAnalisisH.addSpacing(10)

        # PRINCIPAL

        mainLayout = LayoutVCompacto()
        mainLayout.addWidget(toolbar)
        mainLayout.addSpacing(10)
        mainLayout.addLayout(layoutPresupuestoH)
        mainLayout.addSpacing(10)
        mainLayout.addLayout(layoutAnalisisH)
        mainLayout.addSpacing(10)

        self.setLayout(mainLayout)
