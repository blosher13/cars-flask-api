from db import cars
from flask import Flask, request
import uuid
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import get_connection

from schemas import CarSchema

blp = Blueprint("cars", __name__, description="Operations on cars")

# get a list of all cars
@blp.route("/cars")
class Cars(MethodView):
    
    @blp.response(200, CarSchema(many=True))
    def get(self):
        try:
            return cars.values()
        except KeyError:
            abort(404, message='stores not found')

# get a list of a certain make & model using car_id
@blp.route("/cars/<string:store_id>")
def get_make_model(car_id):
    try:
        return cars[car_id]
    except KeyError:
        return {'message': 'Make & Model not found'}, 404
    
# create a car
@app.post('/cars')
def create_car():
    car_data = request.get_json()
    if (
        "make" not in car_data or 
        "model" not in car_data
    ):
        abort(
            400,
            message="Bad request. Ensure 'make', 'model' are included in the JSON payload.",
        )
    for car in cars.values():
        if (
            car_data['make'] == car['make']
            and car_data['model'] == car['model']
        ):
            abort(400, message=f"car already exists.")
    car_id = uuid.uuid4().hex # creates a unique key for each car (ex.d4c8d11c8e364e4597e93dfd2bafcb2b)
    car = {**car_data, 'car_id': car_id}
    cars[car_id] = car # store newly created car inside cars dictionary
    return car

# delete car
@app.delete('/cars/<string:car_id>')
def delete_make_model(car_id):
    try:
        del cars[car_id]
        return {'message': 'car deleted'}
    except KeyError:
        return {'message': 'car_id not found'}, 404