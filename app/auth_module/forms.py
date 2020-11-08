# Import Form and RecaptchaField
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import TextField, PasswordField, BooleanField ,StringField,SubmitField, IntegerField
from wtforms.validators import Required , Email, EqualTo,Length ,DataRequired

#form email field 
from wtforms.fields.html5 import EmailField 
# define the login form (WTFforms)

class LoginForm(FlaskForm):
    username = TextField('Username', [Email(), Required(message='Forgot your username?')])
    password = PasswordField("Password", [Required(message='Must provide a password. ;-)')])
    

class UserRegistrationForm(FlaskForm):
    username=StringField('Username',
    validators=[DataRequired(),Length(min=4,max=25)])

    email = StringField('Email',
    validators=[DataRequired(),Email()])

    password = PasswordField('Password',
    validators=[DataRequired()])

    confirm_password= PasswordField('Confirm Password'
    ,validators=[DataRequired(),EqualTo('password')])

    name = StringField('name')
    Age = IntegerField("age")
    address = StringField("address")
    country = StringField("country")

    submit=SubmitField('Sign Up Auditor')


class AgentRegistrationForm(FlaskForm):
    username=StringField('Username',
    validators=[DataRequired(),Length(min=4,max=25)])

    email = StringField('Email',
    validators=[DataRequired(),Email()])

    password = PasswordField('Password',
    validators=[DataRequired()])

    confirm_password= PasswordField('Confirm Password'
    ,validators=[DataRequired(),EqualTo('password')])

    name = StringField('name')
    Age = IntegerField("age")
    address = StringField("address")
    country = StringField("country")

    submit=SubmitField('Sign Up Agent')


class UserLoginForm(FlaskForm):
    email = StringField('Email',
    validators=[DataRequired(),Email()])

    password = PasswordField('Password',
    validators=[DataRequired()])

    remember = BooleanField('Remember')
    
    submit=SubmitField('Log In User')


class AgentLoginForm(FlaskForm):
    
    email = StringField('Email',
    validators=[DataRequired(),Email()])

    password = PasswordField('Password',
    validators=[DataRequired()])

    remember = BooleanField('Remember')
    
    submit=SubmitField('Log In Agent')     
