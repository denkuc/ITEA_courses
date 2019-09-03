from flask import Flask
from flask_restful import Api
from resources.resources import ProductAPI, CategoryAPI, AllProductsAPI

from mongoengine import connect
connect("products_rest")

app = Flask(__name__)
api = Api(app)

api.add_resource(ProductAPI, "/product/<product_id>")
api.add_resource(CategoryAPI, "/category/<category_id>")
api.add_resource(AllProductsAPI, "/all_products")


if __name__ == '__main__':
    app.run(debug=True)
