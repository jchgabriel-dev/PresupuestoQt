from Visuales.Botones.Botones import BotonAccionMain, BotonAccionSub
from Visuales.Dialogs.Dialogs import DialogElemento
from Visuales.Labels.Labels import LabelDialog, LabelErrorC, LabelIcono
from Visuales.Layouts.Layouts import LayoutVCompacto, LayoutHCompactoAlt, LayoutVSimple, LayoutHCompacto, \
    LayoutHCompactoCen
from Visuales.Lines.Lines import LineElemento
from Visuales.Widgets.Widgets import EspacioH


class CarpetaAgregar(DialogElemento):
    def __init__(self):
        super().__init__("Agregar carpeta", 400, 150)

        mainLayout = LayoutVSimple()
        tituloLayout = LayoutHCompacto()
        titulo = LabelDialog("Ingrese el nombre de la nueva carpeta")
        icono = LabelIcono("agregarCarpeta",30)
        espacio = EspacioH()
        tituloLayout.addWidget(titulo)
        tituloLayout.addItem(espacio)
        tituloLayout.addWidget(icono)

        self.nombre = LineElemento()
        self.error = LabelErrorC("")

        self.agregar = BotonAccionMain("Agregar")
        cancelar = BotonAccionSub("Cancelar")
        cancelar.clicked.connect(self.close)
        botonLayout = LayoutHCompactoAlt()
        botonLayout.addWidget(self.agregar)
        botonLayout.addSpacing(5)
        botonLayout.addWidget(cancelar)

        mainLayout.addLayout(tituloLayout)
        mainLayout.addWidget(self.nombre)
        mainLayout.addSpacing(10)
        mainLayout.addWidget(self.error)
        mainLayout.addSpacing(15)
        mainLayout.addLayout(botonLayout)

        self.setLayout(mainLayout)


class CarpetaEditar(DialogElemento):
    def __init__(self):
        super().__init__("Editar carpeta", 400, 150)

        mainLayout = LayoutVSimple()
        tituloLayout = LayoutHCompacto()
        titulo = LabelDialog("Ingrese el nuevo nombre de la carpeta")
        icono = LabelIcono("editarCarpeta",30)
        espacio = EspacioH()
        tituloLayout.addWidget(titulo)
        tituloLayout.addItem(espacio)
        tituloLayout.addWidget(icono)

        self.nombre = LineElemento()
        self.error = LabelErrorC("")

        self.guardar = BotonAccionMain("Guardar")
        cancelar = BotonAccionSub("Cancelar")
        cancelar.clicked.connect(self.close)
        botonLayout = LayoutHCompactoAlt()
        botonLayout.addWidget(self.guardar)
        botonLayout.addSpacing(5)
        botonLayout.addWidget(cancelar)

        mainLayout.addLayout(tituloLayout)
        mainLayout.addWidget(self.nombre)
        mainLayout.addSpacing(10)
        mainLayout.addWidget(self.error)
        mainLayout.addSpacing(15)
        mainLayout.addLayout(botonLayout)

        self.setLayout(mainLayout)


class CarpetaEliminar(DialogElemento):
    def __init__(self):
        super().__init__("Eliminar carpeta", 400, 150)

        mainLayout = LayoutVSimple()
        tituloLayout = LayoutVCompacto()
        icono = LabelIcono("eliminarCarpeta",40)
        titulo = LabelDialog("¿Estas seguro que deseas eliminar esta carpeta?")
        tituloLayout.addWidget(icono)
        tituloLayout.addSpacing(5)
        tituloLayout.addWidget(titulo)

        self.error = LabelErrorC("")

        self.eliminar = BotonAccionMain("Eliminar")
        cancelar = BotonAccionSub("Cancelar")
        cancelar.clicked.connect(self.close)
        botonLayout = LayoutHCompactoCen()
        botonLayout.addWidget(self.eliminar)
        botonLayout.addSpacing(5)
        botonLayout.addWidget(cancelar)

        mainLayout.addLayout(tituloLayout)
        mainLayout.addSpacing(10)
        mainLayout.addWidget(self.error)
        mainLayout.addSpacing(15)
        mainLayout.addLayout(botonLayout)

        self.setLayout(mainLayout)