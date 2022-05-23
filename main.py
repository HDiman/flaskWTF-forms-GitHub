from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField
# import markupsafe
#
# markupsafe.Markup()
# markupsafe.Markup('')


class LoginForm(FlaskForm):
    email = StringField('Email')
    password = StringField('Password')


app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login")
def login():
    login_form = LoginForm()
    return render_template('login.html', form=login_form)


@app.route("/success")
def success():
    return render_template('success.html')

@app.route("/denied")
def denied():
    return render_template('denied.html')


if __name__ == '__main__':
    app.run(debug=True)
