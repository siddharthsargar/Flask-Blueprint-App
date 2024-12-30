from flask import Flask
from app.auth import auth_bp
from app.admin import admin_bp
from app.public import public_bp
import secrets



def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = secrets.token_hex(32)


    # Register blueprints
    app.register_blueprint(public_bp, url_prefix='/')
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(admin_bp, url_prefix='/admin')


    return app