# Import Flask dependencies
from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for

main_mod = Blueprint('main', __name__, url_prefix="/")

@main_mod.route('/')
def index():
    return render_template('index.html')
@main_mod.route('/contact')
def contact():
    return render_template('contact.html')
@main_mod.route('/post')
def post():
    return render_template('regular.html')
@main_mod.route('/blog')
def blog():
    return render_template('blog.html')