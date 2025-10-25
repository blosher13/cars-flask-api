from flask import Flask
from db import init_db
from cars import blp as CarsBlueprint
# from car_attributes import blp as CarAttributeBlueprint

def create_app():
    app = Flask(__name__)

    # Initialize the database (creates DB and tables)
    init_db()

    # Register blueprints
    app.register_blueprint(CarsBlueprint)
    # app.register_blueprint(CarAttributeBlueprint)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)