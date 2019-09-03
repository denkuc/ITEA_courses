from flask import Flask
from flask_restful import Api
from resources.posts import PostsAPI
from resources.author import AuthorAPI
from mongoengine import connect
connect("posts")

app = Flask(__name__)
api = Api(app)

api.add_resource(PostsAPI, '/post', "/post/<tag>")
api.add_resource(AuthorAPI, '/author', "/author/<nick_name>")


if __name__ == '__main__':
    app.run(debug=True)
