# Import Form and RecaptchaField
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import TextField, PasswordField, BooleanField
from wtforms.validators import Required, Email, EqualTo

# define the login form (WTFforms)

class LoginForm(FlaskForm):
    username = TextField('Username', [Email(), Required(message='Forgot your username?')])
    password = PasswordField("Password", [Required(message='Must provide a password. ;-)')])
    

