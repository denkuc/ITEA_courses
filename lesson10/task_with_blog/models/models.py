from mongoengine import *


class Tag(Document):
    tag = StringField(min_length=3, max_length=30, required=True, regex=r'^\#\w+')


class Author(Document):
    nick_name = StringField(min_length=4, max_length=255, required=True, unique=True)
    first_name = StringField(min_length=4, max_length=255, required=True)
    last_name = StringField(min_length=4, max_length=255, required=True)
    posts = IntField(max_value=9999999)


class Post(Document):
    name = StringField(min_length=4, max_length=255, required=True)
    content = StringField(min_length=10, max_length=1000, required=True)
    datetime = DateTimeField(required=True)
    author = ReferenceField(Author)
    views = IntField(max_value=9999999)
    tag = ListField(ReferenceField(Tag))
