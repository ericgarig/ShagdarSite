"""Main flask app file."""
from flask import Flask

from shagdar_site.blueprints.page import page
from shagdar_site.extensions import csrf, mail


def create_app(settings_override=None):
    """
    Create a Flask application using the app factory pattern.

    :param settings_override: Override settings
    :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.py', silent=True)

    if settings_override:
        app.config.update(settings_override)

    app.register_blueprint(page)
    register_extensions(app)

    return app


def register_extensions(app):
    """
    Register 0 or more extensions (mutates the app passed in).

    :param app: Flask application instance
    :return: None
    """
    csrf.init_app(app)
    mail.init_app(app)

    return None
