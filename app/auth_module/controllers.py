# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for


# Import password / encryption helper tools
from werkzeug.security import check_password_hash, generate_password_hash

# Import the database object from the main app module
from app import db

## Import the login and registeration form for users and agent

# from app.auth_module.forms import UserRegistrationForm,AgentRegistrationForm,UserLoginForm,AgentLoginForm

# Import module forms
from app.auth_module.forms import LoginForm ,RegisterFormAgent,RegisterFormUser

# Import module models (i.e. User)
from app.auth_module.models import User
from app.auth_module.models import Editor


# Define the blueprint: 'auth', set its url prefix: app.url/auth
auth_module = Blueprint('auth', __name__, url_prefix='/auth')

# Set the route and accepted methods
@auth_module.route('/login/', methods=['GET', 'POST'])
def signin():
    # If sign in form is submitted
    form = LoginForm(request.form)
    # Verify the sign in form
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            session['user_id'] = user.id
            flash('Welcome %s' % user.name)
            return redirect(url_for('auth.home'))
        flash('Wrong email or password', 'error-message')
    return render_template("auth/login.html", form=form)

@auth_module.route("/register/", methods=['GET', 'POST'])
def registerUser():
    form =RegisterFormUser(form)
    email=request.form.get('email')
    name= request.form.get('name')
    password=request.form.get('password')
    role=request.form.get('role')
    status=request.form.get('status')
    user= User.query.filter_by(email=email).first()

    if user:
        '''
        if user found then redirect back to signup page so user can try again
        '''
        flash('Email address already exists.')
        return redirect(url_for('auth.signup'))

    new_user= User(email=email,name=name,password=generate_password_hash(password,method='sha256'),role,status)

    ##add new user to the database 
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))

@auth_module.route("/register/",methods=['GET','POST'])
def registerAgent():
    form = RegisterFormAgent(form)
    email=request.form.get('email')
    name= request.form.get('name')
    password=request.form.get('password')

    user= User.query.filter_by(email=email).first()

    if user:
        flash('Email address already exists.')
        return redirect(url_for('auth.signup'))

    new_user= User(email=email,name=name,password=generate_password_hash(password,method='sha256')) 

    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))

