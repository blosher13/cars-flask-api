from flask import Blueprint, request, jsonify
from .. db import db_cursor

blp = Blueprint("car_attributes", __name__)

#get car attributes
@blp.get('/car_attributes')
def get_car_attributes():
    try:
        with db_cursor() as cursor:
            cursor.execute('SELECT * FROM car_attributes')
            rows = cursor.fetchall()
            cursor.close()
        return jsonify(rows)
    except:
        return {'message': 'No car attribute records'}

# create car attributes
@blp.post('/car_attributes')
def create_car_attribute():
    data = request.get_json()
    car_id = data.get('car_id')
    year = data.get('year')
    MSRP_price = data.get('MSRP_price')

    # check to ensure all data is provided in json request
    if not all([car_id, year, MSRP_price]):
        return {"error": "Missing fields"}, 400
    
    with db_cursor() as cursor:

        # check to ensure data is not duplciated
        cursor.execute(
                "SELECT * FROM car_attributes WHERE car_id = %s and year = %s and MSRP_price = %s ", (car_id, year, MSRP_price)
                )
        rows = cursor.fetchone()
        if rows:
            return {"error": "You cannot insert duplciate records"}, 400
        cursor.execute(
            "INSERT INTO car_attributes (car_id, year, MSRP_price) VALUES (%s, %s, %s)",
            (car_id, year, MSRP_price)
        )
        cursor.close()
    return {"message": "Car attribute added successfully"}, 201

# update car attribute
@blp.put('/car_attributes')
def update_car_attribute():
    try:
        data = request.get_json()
        car_id = data.get('car_id')
        year = data.get('year')
        MSRP_price = data.get('MSRP_price')

        with db_cursor() as cursor:
            # check to ensure data is not duplciated
            cursor.execute(
                    "SELECT * FROM car_attributes WHERE car_id = %s and year = %s and MSRP_price = %s ", (car_id, year, MSRP_price)
                    )
            rows = cursor.fetchone()
            if rows:
                return {"error": "You cannot insert duplciate records"}, 400

            cursor.execute(
                '''
                    UPDATE car_attributes
                    SET year = %s, MSRP_price = %s
                    WHERE car_id = %s 
                ''',
                (year, MSRP_price, car_id)
            )
    except KeyError:
        {"error": "Cannot update values"}, 400

# delete car attribute
@blp.delete('/car_attributes')
def delete_make_model():
    try:
        car_id = request.args.get('car_id')
        year = request.args.get('year')
        MSRP_price = request.args.get('MSRP_price')
        
        if not all([car_id, year, MSRP_price]):
            return {"error": "Missing fields"}, 400
        
        with db_cursor() as cursor:
            cursor.execute(
                "DELETE FROM cars WHERE car_id = %s and year = %s and MSRP_price = %s",
                (car_id, year, MSRP_price)
            )
            cursor.close()
        return {"message": "Car attribute removed successfully"}, 201
    except KeyError:
        return {'message': 'Car attribute not removed'}, 404