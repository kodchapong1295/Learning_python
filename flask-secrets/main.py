from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    email = StringField(label='Email')
    password = PasswordField(label='Password')
    submit = SubmitField(label='Log In')

app = Flask(__name__)
app.secret_key = "hello secret world!"

@app.route("/")
def home():
    return render_template('index.html')

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