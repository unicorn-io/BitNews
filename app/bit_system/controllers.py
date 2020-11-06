from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from ipfs import *

bit_system = Blueprint('bit', __name__, url_prefix="/process")

@bit_system.route('/post', methods=['POST'])
def publish():
    title = request.form.get('title')
    content = request.form.get('content')
    url = request.form.get('url')
    urlToImage = request.form.get('urlToImage')
    subject = request.form.get('subject')

    objString = '''
    {
        'title': {title},
        'subject': {subject},
        'content': {content},
        'url': {url},
        'urlToImage': {urlToImage},
    }
    '''.format(title=title, subject=subject, content=content, url=url, urlToImage=urlToImage)
    
    hash = upload_json(objString)
    

