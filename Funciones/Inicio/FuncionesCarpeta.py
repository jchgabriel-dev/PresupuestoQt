from Database.Elementos.ManagerCarpeta import ManagerCarpeta
from Principal.Inicio.Carpeta import CarpetaAgregar, CarpetaEditar, CarpetaEliminar


class FuncionesCarpetaAgregar:
    def __init__(self, carpeta:CarpetaAgregar, id, widget):
        self.id = id
        self.carpeta = carpeta
        self.widget = widget
        self.nombre = self.carpeta.nombre
        self.error = self.carpeta.error
        self.manager = ManagerCarpeta()
        self.carpeta.agregar.clicked.connect(lambda: self.agregarCarpeta())

    def agregarCarpeta(self):
        nombreCarpeta = self.nombre.text().strip()

        if not nombreCarpeta:
            self.error.setText("Ingrese un nombre para la carpeta")
            return False

        hijos = self.manager.listarCarpetaHijo(self.id)
        for id, nombre, padre in hijos:
            if nombre == nombreCarpeta:
                self.error.setText("Ya existe una carpeta con este nombre")
                return False

        id = self.manager.crearCarpeta(nombreCarpeta, self.id)
        self.widget.setIdCarpeta(id)
        self.widget.cargarArbol()
        self.carpeta.close()


class FuncionesCarpetaEditar:
    def __init__(self, carpeta:CarpetaEditar, id, widget):
        self.id = id
        self.carpeta = carpeta
        self.widget = widget
        self.nombre = self.carpeta.nombre
        self.error = self.carpeta.error
        self.manager = ManagerCarpeta()
        self.carpeta.guardar.clicked.connect(lambda: self.editarCarpeta())

    def editarCarpeta(self):
        nombreCarpeta = self.nombre.text().strip()

        if not nombreCarpeta:
            self.error.setText("Ingrese un nombre para la carpeta")
            return False

        hermanos = self.manager.listarCarpetaHermano(self.id)
        for id, nombre, padre in hermanos:
            if nombre == nombreCarpeta:
                self.error.setText("Ya existe una carpeta con este nombre")
                return False

        self.manager.editarCarpeta(nombreCarpeta, self.id)
        self.widget.cargarArbol()
        self.carpeta.close()


class FuncionesCarpetaEliminar:
    def __init__(self, carpeta:CarpetaEliminar, id, widget):
        self.id = id
        self.carpeta = carpeta
        self.widget = widget
        self.error = self.carpeta.error
        self.manager = ManagerCarpeta()
        self.carpeta.eliminar.clicked.connect(lambda: self.eliminarCarpeta())

    def eliminarCarpeta(self):
        hijos = self.manager.listarCarpetaHijo(self.id)

        if hijos:
            self.error.setText("Esta carpeta tiene sub-carpetas")
            return False

        id = self.manager.getPadre(self.id)
        self.widget.setIdCarpeta(id)
        self.manager.eliminarCarpeta(self.id)
        self.widget.cargarArbol()
        self.carpeta.close()
