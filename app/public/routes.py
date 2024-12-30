from flask import render_template
from . import public_bp

@public_bp.route('/')
def index():
    return render_template('index.html')


@public_bp.route('/about')
def about():
    return render_template('about.html')

