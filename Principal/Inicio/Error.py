from PyQt5.QtCore import Qt

from Visuales.Botones.Botones import BotonAccionSub
from Visuales.Dialogs.Dialogs import DialogElemento
from Visuales.Labels.Labels import LabelIcono, LabelDialog
from Visuales.Layouts.Layouts import LayoutVCompacto, LayoutVSimple, LayoutVSimpleCen, LayoutHCompactoCen


class ErrorNormal(DialogElemento):
    def __init__(self, texto):
        super().__init__("Error", 400, 150)

        mainLayout = LayoutVSimpleCen()
        icono = LabelIcono("error", 40)
        titulo = LabelDialog(texto)
        cerrar = BotonAccionSub("Cerrar")
        cerrar.clicked.connect(self.close)
        layoutBoton = LayoutHCompactoCen()
        layoutBoton.addWidget(cerrar)

        mainLayout.addSpacing(5)
        mainLayout.addWidget(icono)
        mainLayout.addSpacing(10)
        mainLayout.addWidget(titulo)
        mainLayout.addSpacing(20)
        mainLayout.addLayout(layoutBoton)
        self.setLayout(mainLayout)
