# Import Flask dependencies
from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for

main_mod = Blueprint('main', __name__, url_prefix="/")

@main_mod.route('/')
def index():
    return render_template('index.html')