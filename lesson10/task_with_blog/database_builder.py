from datetime import datetime
from random import choice
from models.models import Author, Post, Tag

from mongoengine import connect

from data import NICK_NAMES, NAMES, POSTS

connect("posts")


def create_database():
    for nick_name in NICK_NAMES:
        author = Author()
        author.nick_name = nick_name
        author.first_name = choice(NAMES)
        author.last_name = f'{choice(NAMES)}ченко'
        author.posts = 0
        author.save()

    for post_text in POSTS:
        post_words = post_text.split(' ')
        post_words = list(filter(None, post_words))
        post_tags = [word for word in post_words if word[0] == '#']
        tags_ids = []
        for tag_text in post_tags:
            try:
                tag = Tag.objects(tag=tag_text.lower())[0]
            except IndexError:
                tag = Tag()
                tag.tag = tag_text.lower()
                tag.save()
            tags_ids.append(tag.id)

        print(tags_ids)
        post = Post()
        post.name = f'{post_words[0]}_{post_words[1]}'
        post.content = post_text

        author = Author.objects(nick_name=choice(NICK_NAMES))[0]
        author.posts += 1
        author.save()

        post.author = author.id
        post.datetime = datetime.now()
        post.views = 0
        post.tag = tags_ids
        post.save()


create_database()
