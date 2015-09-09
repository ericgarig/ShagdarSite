from flask import Flask

app = Flask(__name__)

# avoid circular references
from app import views