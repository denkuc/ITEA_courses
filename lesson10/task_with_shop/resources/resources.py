from flask_restful import Resource

from models.product import Product, Category
from schemas.product import ProductSchema


class ProductAPI(Resource):
    @staticmethod
    def get(product_id):
        try:
            product = Product.objects(product_id=product_id)[0]
            product.views += 1
            product.save()
            return ProductSchema().dump(product)

        except IndexError:
            return []


class CategoryAPI(Resource):
    @staticmethod
    def get(category_id):
        try:
            category = Category.objects(category_id=category_id)[0]
            products = Product.objects(category=category.id)
            for product in products:
                product.views += 1
                product.save()
            return ProductSchema(many=True).dump(products)

        except IndexError:
            return []


class AllProductsAPI(Resource):
    @staticmethod
    def get():
        try:
            costs_by_product = [p.price*p.items for p in Product.objects()
                                if p.availability]
            total_cost = sum(costs_by_product)

            return {'price_of_all_products': total_cost}

        except IndexError:
            return {}
