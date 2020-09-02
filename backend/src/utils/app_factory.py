from flask import Flask
from flask_cors import CORS
from src.utils.settings import APM_SETTINGS, DEBUG, DB_URL


def build_app():
    app = Flask(__name__)
    app.config['ELASTIC_APM'] = APM_SETTINGS
    app.config['DEBUG'] = DEBUG
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
    app.config['SQLALCHEMY_BINDS'] = {
        'default': DB_URL
    }
    CORS(app)
    return app
