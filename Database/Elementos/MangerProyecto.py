from Database.Database import DatabaseManager


class ManagerProyecto(DatabaseManager):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseManager, cls).__new__(cls)
        return cls._instance

    def crearProyecto(self, nombre):
        self.connect()
        self.cursor.execute("INSERT INTO proyecto (nombre) VALUES (?)", (nombre, ))
        self.connection.commit()
        id = self.cursor.lastrowid
        self.connection.close()
        return id

    def editarProyectoEstado(self, estado, id):
        self.connect()
        self.cursor.execute("UPDATE proyecto SET estado=? WHERE id=?", (estado, id))
        self.connection.commit()
        self.connection.close()

    def eliminarProyecto(self, id):
        self.connect()
        self.cursor.execute("DELETE FROM proyecto WHERE id=?", (id,))
        self.connection.commit()
        self.connection.close()


    def listarProyecto(self):
        self.connect()
        self.cursor.execute("SELECT estado, id, nombre FROM proyecto")
        proyectos = self.cursor.fetchall()
        self.connection.close()
        return proyectos


    def listarProyectoCarpeta(self, id):
        self.connect()
        self.cursor.execute("SELECT estado, id, nombre FROM proyecto WHERE carpeta=?", (id,))
        proyectos = self.cursor.fetchall()
        self.connection.close()
        return proyectos



