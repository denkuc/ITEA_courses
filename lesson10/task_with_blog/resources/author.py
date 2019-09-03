from flask_restful import Resource

from models.models import Post, Author
from schemas.schemas import PostSchema


class AuthorAPI(Resource):
    @staticmethod
    def get(nick_name=None):
        try:
            author_id = Author.objects(nick_name=nick_name)[0].id
            posts = Post.objects(author=author_id)
            for post in posts:
                post.views += 1
                post.save()
            return PostSchema(many=True).dump(posts)
        except IndexError:
            return []

    def post(self):
        pass

    def put(self, id_):
        pass

    def delete(self, id_):
        pass
