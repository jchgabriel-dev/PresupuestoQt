import sqlite3


class DatabaseManager:
    _instance = None

    def __init__(self):
        self.database_file = "Database/Database.data"

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseManager, cls).__new__(cls)
        return cls._instance

    def connect(self):
        self.connection = sqlite3.connect(self.database_file)
        self.cursor = self.connection.cursor()

    def create_database(self):
        self.connect()
        with open('Database/DBInicio.sql', 'r') as archivo_sql:
            sql = archivo_sql.read()
            self.cursor.executescript(sql)

        self.connection.commit()
        self.connection.close()

    def get_database(self):
        return self.database_file









