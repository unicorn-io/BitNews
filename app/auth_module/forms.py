# Import Form and RecaptchaField
from flask_wtf import Form, RecaptchaField
from wtforms import TextField, PasswordField, BooleanField
from wtforms.validators import Required, Email, EqualTo

# define the login form (WTFforms)

class LoginForm(Form):
    email = TextField('Email Address', [Email(), Required(message='Forgot your email address?')])
    password = PasswordField("Password", [Required(message='Must provide a password. ;-)')])
