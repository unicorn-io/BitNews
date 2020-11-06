# Import Form and RecaptchaField
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import TextField, PasswordField, BooleanField ,StringField,SubmitField
from wtforms.validators import DataRequired , Email, EqualTo,Length

# define the login form (WTFforms)

class LoginForm(FlaskForm):
    username = TextField('Username', [Email(), DataRequired(message='Forgot your username?')])
    password = PasswordField("Password", [DataRequired(message='Must provide a password. ;-)')])
    
class RegisterForm(FlaskForm):
    username =TextField('Username',[DataRequired(message='Enter username')])
    email=StringField("Email",[DataRequired(message="Enter a email"),Email()])
    password =PasswordField("Password",[DataRequired(message='Enter a password')])
    role=StringField('Role')
    status=StringField('Status')


    
    
