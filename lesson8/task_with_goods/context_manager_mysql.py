import mysql.connector

config = {'user': 'root',
          'password': 'denkuc',
          'host': '127.0.0.1',
          'database': 'products'}


class CursorMysqlContextManager:
    def __init__(self):
        self.__config = config

    def __enter__(self):
        self.__connection = mysql.connector.connect(**self.__config)
        self.__cursor = self.__connection.cursor()
        return self.__cursor, self.__connection

    def __exit__(self, *args):
        self.__cursor.close()
        self.__connection.close()
