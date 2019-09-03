from mongoengine import *
connect("lesson_9")


class User(Document):
    login = StringField(max_length=30)
    password = StringField(min_length=8, max_length=30)
    email = EmailField(unique=True)
    role = StringField()


class Category(Document):
    title = StringField(max_length=255, unique=True)
    description = StringField(max_length=1024)


class Item(Document):
    added_by = ReferenceField(User)
    category = ReferenceField(Category)
    is_available = BooleanField(default=True)
    name = StringField(required=True, max_length=255)
    description = StringField(max_length=2048, required=False)
    weight = FloatField(required=False)

#
# user = {'login': 'asdasdasd', 'password': 'aaaaaaaa', 'email': 'aaa@a.com', 'role': 'CEO'}
# user_object = User(**user)
# user_object.save()
#
# category = {'title': 'Fruits', 'description': "Fruits bla-bla-bla"}
# category_obj = CategorySerializer(**category)
# category_obj.save()
#
# item = {'added_by': user,
#         'category': category,
#         'is_available': True,
#         'name': 'orange',
#         'description': 'some tasty orange',
#         'weight': 10.0}

# item_obj = Item(**item)
# item_obj.save()


print(Item.objects.filter(category__title='Fruits'))
