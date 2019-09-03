from datetime import datetime
from marshmallow import Schema, validates, ValidationError
from models.models import Post, Tag, Author


class PostSchema(Schema):
    class Meta:
        model = Post
        fields = ['name', 'content', 'datetime', 'views']

    @validates('name')
    def val_name(self, name):
        if len(name) < 4 or len(name) > 255:
            raise ValidationError("ERROR: Post name should be from 4 to 255 chars.")

    @validates('content')
    def val_content(self, content):
        if len(content) < 10 or len(content) > 1000:
            raise ValidationError("ERROR: Post content should be from 10 to 1000 chars.")

    @validates('datetime')
    def val_content(self, datetime_value):
        if not isinstance(datetime_value, datetime):
            raise ValidationError("ERROR: Post datetime should be datetime type.")

    @validates('views')
    def val_views(self, views):
        if not isinstance(views, int):
            raise ValidationError("ERROR: Post views should be int type.")


class TagSchema(Schema):
    class Meta:
        model = Tag
        fields = ['tag']

    @validates('tag')
    def val_tag(self, tag):
        if tag[0] != '#':
            raise ValidationError("ERROR: Tag should start with #")
        if len(tag) < 3 or len(tag) > 30:
            raise ValidationError("ERROR: Tag should be from 4 to 255 chars.")


class AuthorSchema(Schema):
    class Meta:
        model = Author
        fields = ['nick_name', 'first_name', 'last_name', 'posts']

    @validates('nick_name')
    def val_nick_name(self, nick_name):
        if len(nick_name) < 4 or len(nick_name) > 255:
            raise ValidationError("ERROR: Author nick name should be from 4 to 255 chars.")

    @validates('first_name')
    def val_first_name(self, first_name):
        if len(first_name) < 4 or len(first_name) > 255:
            raise ValidationError("ERROR: Author first name should be from 4 to 255 chars.")

    @validates('last_name')
    def val_last_name(self, last_name):
        if len(last_name) < 4 or len(last_name) > 255:
            raise ValidationError("ERROR: Author last name should be from 4 to 255 chars.")

    @validates('posts')
    def val_posts(self, posts):
        if not isinstance(posts, int):
            raise ValidationError("ERROR: Author posts should be int type.")
