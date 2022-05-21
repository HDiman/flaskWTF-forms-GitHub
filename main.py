import markupsafe
from flask import Flask, render_template
from jinja2.environment import Environment
from jinja2.loaders import FileSystemLoader
# from markupsafe import Markup


markupsafe.Markup()
markupsafe.Markup('')


app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login")
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
