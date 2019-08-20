from sqlalchemy.dialects import mysql


class CursorMysqlContextManager:
    def __init__(self, config):
        self.__config = config

    def __enter__(self):
        self.__connection = mysql.connector.connect(self.__config)
        self.__cursor = self.__connection.cursor()
        return self.__connection, self.__cursor

    def __exit__(self, *args):
        self.__cursor.close()
        self.__connection.close()


config_dict = {'user': 'root',
               'password': 'denkuc',
               'host': '127.0.0.1',
               'database': 'students'}

query = """SELECT * FROM student"""

with CursorMysqlContextManager(config_dict) as (cursor, connection):
    cursor.execute(query)
    query_results = cursor.fetchall()
    print(query_results)
