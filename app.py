"""Main app."""
from flask import Flask
from dotenv import load_dotenv

from config import BaseConfig
from blueprints.page import page
from extensions import csrf, mail


def create_app():
    """
    Create a Flask application using the app factory pattern.

    :return: Flask app
    """
    app = Flask(__name__)

    load_dotenv()
    app.config.from_object(BaseConfig)

    app.register_blueprint(page)
    register_extensions(app)

    return app


def register_extensions(app):
    """
    Register extensions.

    :param app: Flask application instance
    :return: None
    """
    csrf.init_app(app)
    mail.init_app(app)
    return None
