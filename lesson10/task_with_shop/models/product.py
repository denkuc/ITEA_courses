from mongoengine import *


class Category(Document):
    category_id = IntField(max_value=999999)
    name = StringField(max_length=255, required=True)
    description = StringField(max_length=1000)
    href = StringField(max_length=1000)


class Product(Document):
    product_id = IntField(max_value=999999)
    name = StringField(max_length=255, required=True)
    price = IntField(max_value=999999)
    availability = BooleanField()
    items = IntField(max_value=999999)
    views = IntField(max_value=999999)
    category = ReferenceField(Category)
