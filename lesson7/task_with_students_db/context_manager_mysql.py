import mysql.connector

config = {'user': 'root',
          'password': 'denkuc',
          'host': '127.0.0.1',
          'database': 'students'}


class MysqlContextManager:
    def __init__(self):
        self.__config = config

    def __enter__(self):
        self.__connection = mysql.connector.connect(**self.__config)
        return self.__connection

    def __exit__(self, *args):
        self.__connection.close()


class CursorContextManager:
    def __init__(self, con):
        self.__connection = con

    def __enter__(self):
        self.__cursor = self.__connection.cursor()
        return self.__cursor

    def __exit__(self, *args):
        self.__cursor.close()
