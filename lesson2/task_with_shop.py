class Shop:
    __network_goods_sold = 0

    def __init__(self, name, goods_sold):
        self.__name = name
        self.__goods_sold = goods_sold
        self.__add_sold_network_goods_sold(goods_sold)

    def get_name(self):
        return self.__name

    @classmethod
    def get_network_goods_sold(cls):
        return cls.__network_goods_sold

    @classmethod
    def __add_sold_network_goods_sold(cls, goods_amount):
        cls.__network_goods_sold += goods_amount

    def get_goods_sold(self):
        return self.__goods_sold

    def sell_goods(self, goods_amount):
        self.__goods_sold += goods_amount
        self.__add_sold_network_goods_sold(goods_amount)


shop1 = Shop('Gulliver', 20)
print(shop1.get_goods_sold())
shop1.sell_goods(45)
print(shop1.get_goods_sold())
print(shop1.get_network_goods_sold())
shop2 = Shop('DreamTown', 30)
shop3 = Shop('SkyMall', 40)

print(Shop.get_network_goods_sold())
