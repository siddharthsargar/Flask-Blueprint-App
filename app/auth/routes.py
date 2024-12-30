from flask import render_template, redirect, url_for
from . import auth_bp


@auth_bp.route('/login')
def login():
    return render_template('login.html')


@auth_bp.route('/register')
def register():
    return render_template('register.html')


