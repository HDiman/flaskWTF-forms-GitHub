from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, InputRequired, Email, Length

# import markupsafe
#
# markupsafe.Markup()
# markupsafe.Markup('')


class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[InputRequired(), Email('Invalid email address')])
    password = PasswordField(label='Password', validators=[InputRequired(), Length(min=8)])
    submit = SubmitField(label='Log In')


app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    # login_form.email.data (for getting certain email)
    if request.method == "GET":
        return render_template('login.html', form=login_form)
    elif request.method == "POST" and login_form.validate_on_submit():
        return render_template('success.html')
    else:
        return render_template('denied.html')


@app.route("/success")
def success():
    return render_template('success.html')

@app.route("/denied")
def denied():
    return render_template('denied.html')


if __name__ == '__main__':
    app.run(debug=True)
