from flask import Flask, request
import json

app = Flask(__name__)

cars = [
    {
        'make':'Toyota',
        'model':'Land Cruiser',
        'vehicle_attributes':[
            {
            'year':'2024',
            'MSRP_price': 69877
            }
        ]
    }
]

@app.get('/cars')
def get_cars():
    return {'cars': cars}

@app.get('/cars/<string:make>/<string:model>')
def get_make_model(make, model):
    clean_model = model.replace(' ', '')
    for car in cars:
        if (car['make'] == make) and (model == clean_model):
            return {'vehicle_attributes': car['vehicle_attributes']}
        else:
            return {'message': 'Make & Model not found'}, 404

@app.post('/cars')
def create_car():
    request_data = request.get_json()
    make = request_data['make']
    model = request_data['model']
    new_car = {'make':make,'model':model, 'vehicle_attributes':[]}
    cars.append(new_car)
    return new_car, 201

@app.post('/cars/<string:make>/<string:model>/vehicle_attributes')
def create_car_attribute(make, model):
    clean_model = model.replace(' ','')
    request_data = request.get_json()
    for car in cars:
        url_model = car['model'].replace(' ','')
        if (car['make'] == make) and (url_model == clean_model):
            new_attribute_year = request_data['year']
            new_attribute_price = request_data['MSRP_price']
            new_attribute_vehicle = {'year':new_attribute_year, 'MSRP_price': new_attribute_price}
            car['vehicle_attributes'].append(new_attribute_vehicle)
            return new_attribute_vehicle, 201
        else:
            return {'message': 'Make & Model not found'}, 404

app.run(debug=True)
