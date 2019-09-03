from context_manager_mysql import CursorMysqlContextManager


class Product:
    def __init__(self):
        self.__id = None
        self.__name = None
        self.__description = None
        self.__category_id = None
        self.__available = None
        self.__price = None
        self.__amount = None

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

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = description

    @property
    def category_id(self):
        return self.__category_id

    @category_id.setter
    def category_id(self, category_id):
        self.__category_id = category_id

    @property
    def available(self):
        return self.__available

    @available.setter
    def available(self, available):
        self.__available = available

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, amount):
        self.__amount = amount


class ProductSerializer:
    __index_id = 0
    __index_name = 1
    __index_description = 2
    __index_category_id = 3
    __index_available = 4
    __index_price = 5
    __index_amount = 6

    def get_products_by_category(self, category_id):
        products_query = f"""SELECT * FROM product 
                             WHERE category_id = {category_id}
                             AND available = TRUE"""
        with CursorMysqlContextManager() as (cursor, connection):
            cursor.execute(products_query)
            product_tuples = cursor.fetchall()

            return [self.__get_deserialized_product(product)
                    for product in product_tuples]

    def add_product(self, product):
        add_product_query = """INSERT INTO product 
                               VALUES ({}, '{}', '{}', {}, {}, {}, {})"""
        product_tuple = self.__get_serialized_product(product)
        add_product_query = add_product_query.format(*product_tuple)
        with CursorMysqlContextManager() as (cursor, connection):
            cursor.execute(add_product_query)
            connection.commit()

    def get_product_by_id(self, id_):
        product_query = f"""SELECT * FROM product WHERE id = {id_}"""
        with CursorMysqlContextManager() as (cursor, connection):
            cursor.execute(product_query)
            product_tuple = cursor.fetchone()

            return self.__get_deserialized_product(product_tuple)

    def __get_deserialized_product(self, product_tuple):
        product = Product()
        product.id = product_tuple[self.__index_id]
        product.name = product_tuple[self.__index_name]
        product.description = product_tuple[self.__index_description]
        product.category_id = product_tuple[self.__index_category_id]
        product.available = product_tuple[self.__index_available]
        product.price = product_tuple[self.__index_price] / 100
        product.amount = product_tuple[self.__index_amount]

        return product

    @staticmethod
    def __get_serialized_product(product):
        return (product.id,
                product.name,
                product.description,
                product.category_id,
                product.available,
                product.price,
                product.amount)
