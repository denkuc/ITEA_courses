from marshmallow import Schema
from models.product import Product


class ProductSchema(Schema):
    class Meta:
        model = Product
        fields = ['product_id', 'name', 'views', 'price',
                  'items', 'availability']
