from Database.Database import DatabaseManager


class ManagerCarpeta(DatabaseManager):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseManager, cls).__new__(cls)
        return cls._instance

    def crearCarpeta(self, nombre, padre=None):
        self.connect()
        self.cursor.execute("INSERT INTO carpeta (nombre, padre) VALUES (?, ?)", (nombre, padre))
        self.connection.commit()
        id = self.cursor.lastrowid
        self.connection.close()
        return id

    def editarCarpeta(self, nombre, id):
        self.connect()
        self.cursor.execute("UPDATE carpeta SET nombre=? WHERE id=?", (nombre, id))
        self.connection.commit()
        self.connection.close()

    def eliminarCarpeta(self, id):
        self.connect()
        self.cursor.execute("DELETE FROM carpeta WHERE id=?", (id,))
        self.connection.commit()
        self.connection.close()

    def listarCarpetaHijo(self, id):
        self.connect()
        self.cursor.execute("SELECT id, nombre, padre FROM carpeta WHERE padre=?", (id,))
        carpetas = self.cursor.fetchall()
        self.connection.close()
        return carpetas

    def listarCarpeta(self):
        self.connect()
        self.cursor.execute("SELECT * FROM carpeta")
        carpetas = self.cursor.fetchall()
        self.connection.close()
        return carpetas



    def listarCarpetaHermano(self, id):
        padre = self.getPadre(id)
        self.connect()
        self.cursor.execute("SELECT id, nombre, padre FROM carpeta WHERE padre=?", (padre,))
        carpetas = self.cursor.fetchall()
        self.connection.close()
        return carpetas

    def getPadre(self, id):
        self.connect()
        self.cursor.execute("SELECT padre FROM carpeta WHERE id=?", (id,))
        padre = self.cursor.fetchone()[0]
        self.connection.close()
        return padre

