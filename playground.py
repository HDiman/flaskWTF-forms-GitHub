import markupsafe
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

from jinja2.environment import Environment
from jinja2.loaders import FileSystemLoader
from markupsafe import Markup
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename



markupsafe.Markup()
markupsafe.Markup('')


app = Flask(__name__)

class MyForm(FlaskForm):
    user_email = StringField(label=('Email'))
    user_login = StringField(label=('Password'))
    submit = SubmitField(label=('Log In'))


try:
    @app.route("/")
    def home():
        return render_template('index.html')

    @app.route("/login")
    def login():
        return render_template('login.html')
except ImportError:
    pass

if __name__ == '__main__':
    app.run(debug=True)


# Trying yield

def return_squeard(min, max):
    for i in range(min, max):
        yield i**2

result = return_squeard(1, 5)

print(next(result))
print(next(result))
print(next(result))