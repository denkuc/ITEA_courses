from flask import Flask, request
from flask import render_template
app = Flask(__name__)


@app.route('/')
@app.route('/index', methods=["GET", "POST"])
def index():
    print(dict(request.form))
    return render_template("form_example.html")


if __name__ == '__main__':
    app.run(debug=True)
