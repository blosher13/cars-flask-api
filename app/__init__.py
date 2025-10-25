from flask import Flask
from .db import init_db
from .routes.cars import blp as CarsBlueprint
from .routes.car_attributes import blp as CarAttributeBlueprint

def create_app():
    app = Flask(__name__)

    # Initialize the database (creates DB and tables)
    init_db()

    # Register blueprints
    app.register_blueprint(CarsBlueprint)
    app.register_blueprint(CarAttributeBlueprint)

    return app