from flask import Flask
from config import config
from .db import mongo
from .routes import configure_routes


def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config[config_name])

    mongo.init_app(app)

    configure_routes(app)

    return app
