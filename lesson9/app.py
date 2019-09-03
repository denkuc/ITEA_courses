from flask import Flask
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return json.dumps({'test': ['aaa', 'bbb']})


if __name__ == '__main__':
    app.run()
