from marshmallow import Schema, fields

class CarSchema(Schema):
    car_id = fields.Str(dump_only=True)
    make = fields.Str(required=True)
    model = fields.Str(required=True)

class CarAttributeSchema(Schema):
    car_attribute_id = fields.Str(dump_only=True)
    car_id = fields.Str(required=True)
    year = fields.Str(required=True)
    MSRP_price = fields.Str(required=True)

class CarAttributeUpdateSchema(Schema):
    car_attribute_id = fields.Str(dump_only=True)
    car_id = fields.Str(required=True)
    year = fields.Str()
    MSRP_price = fields.Str()
