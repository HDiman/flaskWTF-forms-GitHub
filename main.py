# from flask import Flask, render_template, request
# from flask_wtf import FlaskForm
# from wtforms import StringField, PasswordField, SubmitField
# from wtforms.validators import DataRequired, InputRequired, Email, Length
# from flask_bootstrap import Bootstrap
#
# # import markupsafe
# #
# # markupsafe.Markup()
# # markupsafe.Markup('')
#
# # def create_app():
# #     app = Flask(__name__)
# #     app.secret_key = "any-string-you-want-just-keep-it-secret"
# #     Bootstrap(app)
# #
# #     return app
#
#
# class LoginForm(FlaskForm):
#     email = StringField(label='Email', validators=[InputRequired(), Email('Invalid email address')])
#     password = PasswordField(label='Password', validators=[InputRequired(), Length(min=8)])
#     submit = SubmitField(label='Log In')
#
# app = Flask(__name__)
# app.secret_key = "any-string-you-want-just-keep-it-secret"
# Bootstrap(app)
#
# @app.route("/")
# def home():
#     return render_template("index.html")
#
#
# @app.route("/login", methods=["GET", "POST"])
# def login():
#     login_form = LoginForm()
#     # login_form.email.data (for getting certain email)
#     if request.method == "GET":
#         return render_template('login.html', form=login_form)
#     elif request.method == "POST" and login_form.validate_on_submit():
#         return render_template('success.html')
#     else:
#         return render_template('denied.html')
#
#
# @app.route("/success")
# def success():
#     return render_template('success.html')
#
# @app.route("/denied")
# def denied():
#     return render_template('denied.html')
#
#
# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap


class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label="Log In")


app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"
Bootstrap(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=login_form)


if __name__ == '__main__':
    app.run(debug=True)