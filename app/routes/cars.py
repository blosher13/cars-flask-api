from flask import Blueprint, request, jsonify
from .. db import db_cursor

blp = Blueprint("cars", __name__)

# get a list of all cars
@blp.get("/cars")
def get_all_cars():
    try:
        with db_cursor() as cursor:
            cursor.execute("SELECT * FROM cars")
            rows = cursor.fetchall()
            cursor.close()
        return jsonify(rows)
    except:
        return {'message': 'No car records'}

# get a list of a certain make & model using car_id
@blp.get("/cars")
def get_a_car(make, model):
    try:
        make = request.args.get('make')
        model = request.args.get('model')
        with db_cursor() as cursor:
            cursor.execute(
                "SELECT * FROM cars WHERE make = %s and model = %s ", (make, model)
                )
            rows = cursor.fetchall()
            cursor.close()
        return jsonify(rows)
    except KeyError:
        return {'message': 'Make & Model not found'}, 404
    
# create a car
@blp.post('/cars')
def create_car():
    data = request.get_json()
    # car_id = uuid.uuid4().hex # creates a unique key for each car (ex.d4c8d11c8e364e4597e93dfd2bafcb2b)
    make = data.get("make")
    model = data.get("model")

    if not all([make, model]):
        return {"error": "Missing fields"}, 400
    
    with db_cursor() as cursor:
        cursor.execute(
            "INSERT INTO cars (make, model) VALUES (%s, %s)",
            (make, model)
        )
        cursor.close()
    return {"message": "Car added successfully"}, 201

# delete car
@blp.delete('/cars')
def delete_make_model():
    try:
        make = request.args.get('make')
        model = request.args.get('model')
        
        if not all([make, model]):
            return {"error": "Missing fields"}, 400
        
        with db_cursor() as cursor:
            cursor.execute(
                "DELETE FROM cars WHERE make = %s and model = %s",
                (make, model)
            )
            cursor.close()
        return {"message": "Car removed successfully"}, 201
    except KeyError:
        return {'message': 'Car not removed'}, 404
