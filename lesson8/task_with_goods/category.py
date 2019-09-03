from context_manager_mysql import CursorMysqlContextManager


class Category:
    def __init__(self) -> None:
        self.__id = None
        self.__name = None

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id_):
        self.__id = id_

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name


class CategorySerializer:
    __index_id = 0
    __index_name = 1

    def get_all_categories(self) -> list:
        categories_query = """SELECT * FROM category"""
        with CursorMysqlContextManager() as (cursor, connection):
            cursor.execute(categories_query)
            category_tuples = cursor.fetchall()

            return [self.__get_deserialized_category(category)
                    for category in category_tuples]

    def get_category_by_id(self, id_):
        category_query = f"""SELECT * FROM category WHERE id = {id_}"""
        with CursorMysqlContextManager() as (cursor, connection):
            cursor.execute(category_query)
            category_tuple = cursor.fetchone()

            return self.__get_deserialized_category(category_tuple)

    def add_category(self, category):
        add_category_query = """INSERT INTO category VALUES ({}, '{}')"""
        category_tuple = self.__get_serialized_category(category)
        add_category_query = add_category_query.format(*category_tuple)
        with CursorMysqlContextManager() as (cursor, connection):
            cursor.execute(add_category_query)
            connection.commit()

    def __get_deserialized_category(self, category_tuple):
        category = Category()
        category.id = category_tuple[self.__index_id]
        category.name = category_tuple[self.__index_name]

        return category

    @staticmethod
    def __get_serialized_category(category):
        return (category.id,
                category.name)
