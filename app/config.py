import os

from app.utils.functions import as_bool


class BaseConfig(object):
    APP_NAME = os.environ.get("APP_NAME", "ShagdarSite")
    DEBUG = os.environ.get("DEBUG", 1)
    SECRET_KEY = os.environ.get("SECRET_KEY")

    MAIL_SERVER = os.environ.get("MAIL_SERVER")
    MAIL_PORT = int(os.environ.get("MAIL_PORT"))
    MAIL_USE_TLS = as_bool(os.environ.get("MAIL_USE_TLS"))
    MAIL_USE_SSL = as_bool(os.environ.get("MAIL_USE_SSL"))
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    MAIL_DEBUG = int(os.environ.get("MAIL_DEBUG", 1))

    SEND_MAIL_TO = os.environ.get("SEND_MAIL_TO")

    RECAPTCHA_PUBLIC_KEY = os.environ.get("RECAPTCHA_PUBLIC_KEY")
    RECAPTCHA_PRIVATE_KEY = os.environ.get("RECAPTCHA_PRIVATE_KEY")
