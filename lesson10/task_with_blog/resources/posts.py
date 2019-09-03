from flask_restful import Resource

from models.models import Tag, Post
from schemas.schemas import PostSchema


class PostsAPI(Resource):
    @staticmethod
    def get(tag=None):
        try:
            tag_id = Tag.objects(tag='#'+tag.lower())[0].id
            posts = Post.objects(tag=tag_id)
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
