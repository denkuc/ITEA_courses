from random import randint

from mongoengine import connect

import requests as r
from bs4 import BeautifulSoup

from models.product import Category, Product

connect("products_rest")

SHOP_URL = 'http://fankyshop.net'


def create_categories():
    shop_html = r.get(SHOP_URL).content
    soup = BeautifulSoup(shop_html)
    menu_tag = soup.find('div', attrs={'class': 'menu'})
    category_tags = menu_tag.find_all('a')
    category_id = 0
    for category_tag in category_tags:
        category_name = category_tag.text
        try:
            Category.objects(name=category_name)[0]
        except IndexError:
            category_obj = Category()
            category_obj.href = category_tag.get('href')
            category_obj.name = category_tag.text
            category_obj.category_id = category_id
            category_soup = BeautifulSoup(r.get(f'{SHOP_URL}{category_obj.href}').content)
            try:
                category_desc = category_soup.find('div', {'class': 'categoryDesc'}).find('p').text
                category_obj.description = category_desc
            except:
                category_obj.description = 'Default description'
            category_obj.save()
            category_id += 1


def change_href_for_categories():
    new_href = {
        'Мужская обувь': '/c862-muzhskie_tufli_zara',
        'Женская обувь': '/c553-zhenskie_zimnie_sapogi_uggi_ugg',
        'Распродажа обуви': '/c373-rasprodazha_muzhskoy_obuvi',
        'Футболки': '/c836-futbolki_s_gruppami'
    }
    for category_name, href in new_href.items():
        category = Category.objects(name=category_name)[0]
        category.href = href
        category.save()


def create_products():
    product_id = 0
    for category_obj in Category.objects():
        category_soup = BeautifulSoup(r.get(f'{SHOP_URL}{category_obj.href}').content)
        product_tags = category_soup.find_all('td', {'class': 'prodWrap'})
        for product_tag in product_tags:
            product_obj = Product()
            product_obj.product_id = product_id
            product_obj.category = category_obj
            product_obj.items = randint(0, 10)
            product_obj.availability = (product_obj.items != 0)
            product_obj.views = 0

            product_name = product_tag.find('div', {'class': 'productsname'}).\
                find('a').text
            product_obj.name = product_name
            print(product_name)
            try:
                product_price = product_tag.find('span', {'class': 'price'}).\
                    find('b', {'class': 'int'}).text
            except:
                break
            product_price = product_price.replace('\xa0', '')
            product_obj.price = int(product_price)

            product_obj.save()

            product_id += 1


create_categories()
change_href_for_categories()
create_products()
