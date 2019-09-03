from random import randint

from flask import Flask, render_template, url_for, request

from category import CategorySerializer, Category
from product import ProductSerializer, Product

app = Flask(__name__)
app._static_folder = 'lesson8/task_with_goods'


@app.route('/')
@app.route('/index')
@app.route('/categories')
def index():
    categories = CategorySerializer().get_all_categories()
    categories = [{'href': url_for('route_category', category_id=category.id),
                   'name': category.name}
                  for category in categories]
    return render_template("categories.html", categories=categories)


@app.route('/category/<category_id>', methods=['GET'])
def route_category(category_id):
    product_serializer = ProductSerializer()
    category_serializer = CategorySerializer()

    category_name = category_serializer.get_category_by_id(category_id).name

    products = product_serializer.get_products_by_category(category_id)
    products = [{'href': url_for('route_product', product_id=product.id),
                 'name': product.name}
                for product in products]
    return render_template("category.html",
                           products=products,
                           category_name=category_name)


@app.route('/product/<product_id>', methods=['GET'])
def route_product(product_id):
    product_serializer = ProductSerializer()

    product = product_serializer.get_product_by_id(product_id)
    product = {'category_href': url_for('route_category',
                                        category_id=product.category_id),
               'name': product.name,
               'description': product.description,
               'amount': product.amount,
               'price': product.price}
    return render_template("product.html", product=product)


@app.route('/admin', methods=['GET'])
def route_admin():
    return render_template("admin.html")


@app.route('/add_category', methods=['POST'])
def add_category():
    category = Category()
    category.id = randint(0, 999999)
    category.name = request.form['name']
    CategorySerializer().add_category(category)

    return render_template("admin.html")


@app.route('/add_product', methods=['POST'])
def add_product():
    product = Product()
    product.id = randint(0, 999999)
    product.name = request.form['name']
    product.description = request.form['description']
    if request.form['available'] == 'on':
        product.available = 1
    else:
        product.available = 0
    product.price = request.form['price']
    product.amount = request.form['amount']
    product.category_id = request.form['category_id']
    ProductSerializer().add_product(product)

    return render_template("admin.html")


if __name__ == '__main__':
    app.run(debug=True)
