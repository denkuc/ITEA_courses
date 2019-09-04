from mongoengine import Document, StringField, IntField, EmailField, ListField


class User(Document):
    telegram_id = IntField(max_value=99999999999)
    state = StringField(max_length=255)
    name = StringField(max_length=255)
    email = EmailField()
    phone_number = IntField(max_value=99999999999)
    address = StringField(max_length=255)
    suggestions = ListField(StringField(max_length=1000))
