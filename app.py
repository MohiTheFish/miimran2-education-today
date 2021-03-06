# Import the required libraries
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS


# Create various application instances
# Order matters: Initialize SQLAlchemy before Marshmallow
db = SQLAlchemy()
ma = Marshmallow()
cors = CORS()


def create_app():
    """Application-factory pattern"""
    app = Flask(__name__, static_url_path='', static_folder='client/build')
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:password@localhost:3306/education-today-miimran2"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    # To use the application instances above, instantiate with an application:
    db.init_app(app)
    ma.init_app(app)
    cors.init_app(app)

    return app