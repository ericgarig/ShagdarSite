from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
app.config.from_object('config')

mail = Mail(app)

from views import *


if __name__ == '__main.py__':
    app.run()
