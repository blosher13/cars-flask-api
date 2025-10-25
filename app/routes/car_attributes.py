from flask import Flask, request
import uuid
from flask.views import MethodView
from flask_smorest import Blueprint, abort

blp = Blueprint("car_attributes", __name__, description="Operations on car_attributes")

#get car attributes
@app.get('/car_attributes')
def get_car_attributes():
    try:
        return {'car_attributes': list(car_attributes.values())}
    except:
        return {'message': 'No car attributes'}

# create car attributes
@app.post('/car_attributes')
def create_car_attribute():
    car_attribute_data = request.get_json()
    if (
        "car_id" not in car_attribute_data or 
        "year" not in car_attribute_data or 
        "MSRP_price" not in car_attribute_data
        ):
        abort(
            400,
            message="Bad request. Ensure 'car_id', 'year', and 'MSRP_price' are included in the JSON payload.",
        )
    for car_attribute in car_attributes['car_attributes']:
        if (
            car_attribute_data['year'] == car_attribute['year']
            and car_attribute_data['MSRP_price'] == car_attribute['MSRP_price']
        ):
            abort(400, message=f"attribute already exists.")

    car_attribute_id = uuid.uuid4().hex
    car_attribute = {**car_attribute_data, 'car_attribute_id': car_attribute_id}
    car_attributes[car_attribute_id] = car_attribute
    return car_attribute

# update car attribute
@app.put('/car_attributes/<string:car_attribute_id>')
def update_car_attribute(car_attribute_id):
    car_attribute_data = request.get_json()
    if (
        "car_id" not in car_attribute_data or 
        "year" not in car_attribute_data or 
        "MSRP_price" not in car_attribute_data
        ):
        abort(
            400,
            message="Bad request. Ensure 'car_id', 'year', and 'MSRP_price' are included in the JSON payload.",
        )
    try:
        for va in car_attributes["car_attributes"]:
            if va['car_attribute_id'] == car_attribute_id:
                va.update(car_attribute_data)
            return va
    except KeyError:
        abort(404, message='car attribute not found')