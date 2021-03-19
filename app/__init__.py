from flask import Flask
from config import config
from .db import mongo
import logging


def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config[config_name])

    mongo.init_app(app)

    from .routes import configure_routes
    configure_routes(app)

    return app
