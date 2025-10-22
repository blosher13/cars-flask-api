from flask import Flask, request
import uuid
from flask_smorest import abort

from db import cars, vehicle_attributes

app = Flask(__name__)

# get a list of all cars
@app.get('/cars')
def get_all_cars():
    return {'cars': list(cars.values())}

# get a list of a certain make & model using car_id
@app.get('/cars/<string:car_id>')
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
            abort(400, message=f"vehicle already exists.")
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

#get car attributes
@app.get('/vehicle_attributes')
def get_car_attributes():
    try:
        return {'vehicle_attributes': list(vehicle_attributes.values())}
    except:
        return {'message': 'No vehicle attributes'}

# create car attributes
@app.post('/vehicle_attributes')
def create_car_attribute():
    vehicle_attribute_data = request.get_json()
    if (
        "car_id" not in vehicle_attribute_data or 
        "year" not in vehicle_attribute_data or 
        "MSRP_price" not in vehicle_attribute_data
        ):
        abort(
            400,
            message="Bad request. Ensure 'car_id', 'year', and 'MSRP_price' are included in the JSON payload.",
        )
    for vehicle_attribute in vehicle_attributes['vehicle_attributes']:
        if (
            vehicle_attribute_data['year'] == vehicle_attribute['year']
            and vehicle_attribute_data['MSRP_price'] == vehicle_attribute['MSRP_price']
        ):
            abort(400, message=f"attribute already exists.")

    vehicle_attribute_id = uuid.uuid4().hex
    vehicle_attribute = {**vehicle_attribute_data, 'vehicle_attribute_id': vehicle_attribute_id}
    vehicle_attributes[vehicle_attribute_id] = vehicle_attribute
    return vehicle_attribute

# update vehicle attribute
@app.put('/vehicle_attributes/<string:vehicle_attribute_id>')
def update_vehicle_attribute(vehicle_attribute_id):
    vehicle_attribute_data = request.get_json()
    if (
        "car_id" not in vehicle_attribute_data or 
        "year" not in vehicle_attribute_data or 
        "MSRP_price" not in vehicle_attribute_data
        ):
        abort(
            400,
            message="Bad request. Ensure 'car_id', 'year', and 'MSRP_price' are included in the JSON payload.",
        )
    try:
        for va in vehicle_attributes["vehicle_attributes"]:
            if va['vehicle_attribute_id'] == vehicle_attribute_id:
                va.update(vehicle_attribute_data)
            return va
    except KeyError:
        abort(404, message='vehicle attribute not found')

app.run(debug=True)