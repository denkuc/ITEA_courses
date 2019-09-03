from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    info = {'a': 1}
    return f"""
    <html>
        <head>
            <title></title>
            <body>
                <center><h1>{info['a']}</h1></center>
            </body>
        </head>
    </html>
    """


if __name__ == '__main__':
    app.run()
