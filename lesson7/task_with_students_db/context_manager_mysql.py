import mysql.connector

config = {'user': 'root',
          'password': 'denkuc',
          'host': '127.0.0.1',
          'database': 'students'}


class CursorMysqlContextManager:
    def __init__(self):
        self.__config = config

    def __enter__(self):
        self.__connection = mysql.connector.connect(**self.__config)
        self.__cursor = self.__connection.cursor()
        return self.__connection, self.__cursor

    def __exit__(self, *args):
        self.__cursor.close()
        self.__connection.close()
