from sqlalchemy.dialects import mysql


class MysqlContextManager:
    def __init__(self, config):
        self.__config = config

    def __enter__(self):
        self.__connection = mysql.connector.connect(self.__config)
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


config = {'user': 'root',
          'password': 'password',
          'host': '127.0.0.1',
          'database': 'employees'}

query = """SELECT * FROM employees"""

with MysqlContextManager(config) as con:
    with CursorContextManager(con) as cursor:
        cursor.execute(query)
        query_results = cursor.fetchall()
        print(query_results)
