from Database.Database import DatabaseManager


class ManagerSubPresupuesto(DatabaseManager):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseManager, cls).__new__(cls)
        return cls._instance

    def crearSubPresupuesto(self, nombre):
        self.connect()
        self.cursor.execute("INSERT INTO subPresupuesto (nombre) VALUES (?)", (nombre, ))
        self.connection.commit()
        id = self.cursor.lastrowid
        self.connection.close()
        return id

    def editarSubPresupuesto(self, estado, id):
        self.connect()
        self.cursor.execute("UPDATE subPresupuesto SET estado=? WHERE id=?", (estado, id))
        self.connection.commit()
        self.connection.close()

    def eliminarSubPresupuesto(self, id):
        self.connect()
        self.cursor.execute("DELETE FROM subPresupuesto WHERE id=?", (id,))
        self.connection.commit()
        self.connection.close()

    def listarSubPresupuestoProyecto(self, id):
        self.connect()
        self.cursor.execute("SELECT id, orden, nombre FROM subPresupuesto WHERE proyecto=?", (id,))
        subPresupuestos = self.cursor.fetchall()
        self.connection.close()
        return subPresupuestos






