from flask import Flask
from config import config
from .routes import configure_routes


def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config[config_name])

    configure_routes(app)

    return app
