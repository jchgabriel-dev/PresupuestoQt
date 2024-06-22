from Database.Database import DatabaseManager


class ManagerEstado(DatabaseManager):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseManager, cls).__new__(cls)
        return cls._instance

    def listarEstado(self):
        self.connect()
        self.cursor.execute("SELECT * FROM estado")
        estados = self.cursor.fetchall()
        self.connection.close()
        return estados

