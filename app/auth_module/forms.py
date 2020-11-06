# Import Form and RecaptchaField
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import TextField, PasswordField, BooleanField ,StringField,SubmitField
from wtforms.validators import Required , Email, EqualTo,Length ,DataRequired

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

    role=StringField('Role',
    validators=[DataRequired()])

    status=StringField('Status',
    validators=[DataRequired()])

    submit=SubmitField('Sign Up User')


class AgentRegistrationForm(FlaskForm):
    username=StringField('Username',
    validators=[DataRequired(),Length(min=4,max=25)])

    email = StringField('Email',
    validators=[DataRequired(),Email()])

    password = PasswordField('Password',
    validators=[DataRequired()])

    confirm_password= PasswordField('Confirm Password'
    ,validators=[DataRequired(),EqualTo('password')])

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
