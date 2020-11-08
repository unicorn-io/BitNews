# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
# Import password / encryption helper tools
from werkzeug.security import check_password_hash, generate_password_hash

# Import the database object from the main app module
from app import db

# Import module forms
from app.auth_module.forms import LoginForm, UserRegistrationForm, AgentRegistrationForm    

# Import module models (i.e. User)
from app.auth_module.models import User
from app.auth_module.models import Editor

# Define the blueprint: 'auth', set its url prefix: app.url/auth
auth_module = Blueprint('auth', __name__, url_prefix='/auth')

@auth_module.route("/login")
def login():
    form = LoginForm(request.form)
    return render_template("auth/login.html", form=form)

# Set the route and accepted methods
@auth_module.route('/login_auditor', methods=['GET', 'POST'])
def signin_auditor():
    return render_template('/auditor_index.html')
    # If sign in form is submitted
    form = LoginForm(request.form)
    remember = True if request.form.get("remember") else False
    # Verify the sign in form
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            session['user_id'] = user.id
            login_user(user, remember=remember)
            return render_template('auditor_index.html')
        flash('Wrong email or password', 'error-message')
    return render_template("auth/login.html", form=form)

@auth_module.route('/login_editor', methods=['GET', 'POST'])
def signin_editor():
    # If sign in form is submitted
    form = LoginForm(request.form)
    remember = True if request.form.get("remember") else False
    # Verify the sign in form
    if form.validate_on_submit():
        editor = Editor.query.filter_by(email=form.email.data).first()
        if editor and check_password_hash(editor.password, form.password.data):
            session['user_id'] = editor.id
            login_user(editor, remember=remember)
            return render_template('agent_index.html')
        flash('Wrong email or password', 'error-message')
    return render_template("auth/login.html", form=form)


@auth_module.route("/register/", methods=['GET', 'POST'])
def register():
    return render_template("auth/register.html")

@auth_module.route('/logout')
def logout():
    logout_user()
    return redirect("/")

@auth_module.route('/register')
def register_page():
    return render_template("register.html")


@auth_module.route('/register_auditor', methods=['GET', 'POST'])
def register_user():
    if current_user.is_authenticated:
        return redirect("/")
    form = UserRegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)