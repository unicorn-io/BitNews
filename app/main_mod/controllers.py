# Import Flask dependencies
from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from .ipfs import *
from .news import *

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

@main_mod.route('/agentIndex')
def agentIndex():
    return render_template('agent_index.html')

@main_mod.route('/auditorIndex')
def auditorIndex():
    return render_template('auditor_index.html')
    
@main_mod.route('./procedure')
def procedure():
    return render_template('procedure.html')

@main_mod.route('/new-post')
def agentPost():
    return render_template('agent_post.html')

@main_mod.route('/view-post', methods=["GET"])
def view_post():
    hash = request.args.get('q')
    real = request.args.get('real')
    real = 'Real' if real != 1 else 'Not Decided'
    data = get_json(hash)
    return render_template('regular.html', title=data['title'],content=data['content'], url=data['url'], urlToImage=data['urlToImage'], hash=hash, real=real)
