from pathlib import Path

import toml
from flask import Flask

from .routes import routes

app = Flask(__name__)

with open(Path.cwd() / '.secrets.toml', 'r', encoding='utf-8') as file:
    _secret_key = toml.load(file).get('FLASK_SECRET_KEY')

app.secret_key = _secret_key

app.register_blueprint(routes)
