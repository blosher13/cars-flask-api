"""
db.py
---

Later on, this file will be replaced by SQLAlchemy. For now, it mimics a database.
Our data storage is:
    - stores have a unique ID and a name
    - items have a unique ID, a name, a price, and a store ID.
cars ={
    1:{
        'make':'Toyota',
        'model':'Land Cruiser',
        'vehicle_attributes':[
            {
            'year': 2024,
            'MSRP_price': 69877
            }
        ]
    },
    2: {
        'make':'Chevy',
        'model':'Suburban',
        'vehicle_attributes':[
            {
            'year': 2024,
            'MSRP_price': 89877
            }
        ]
    }
    }
    """

cars ={
    "f840f9bc485a441c889781fba00bb84e": {
        "car_id": "f840f9bc485a441c889781fba00bb84e",
        "make": "Toyota",
        "model": "Corolla"
    },
    "fa21f7befa254691b606a48b2beb4272": {
        "car_id": "fa21f7befa254691b606a48b2beb4272",
        "make": "Toyota",
        "model": "Camry"
    }
}

# {
#     "cars": [
#         {
#             "car_id": "522ad1b7789d4080961c79d1a41c4f5f",
#             "make": "Toyota",
#             "model": "Corolla"
#         },
#         {
#             "car_id": "e3b40f29836444d986f5da4310ae7d74",
#             "make": "Toyota",
#             "model": "Camry"
#         }
#     ]
# }
vehicle_attributes = {
    "vehicle_attributes": [
        {
            "MSRP_price": 42000,
            "car_id": "f7c18433aacb49ee9140214aa823cad5",
            "vehicle_attribute_id": "111e951d1c2244b6b5e9bea33e471739",
            "year": "2025"
        },
        {
            "MSRP_price": 30000,
            "car_id": "e3b40f29836444d986f5da4310ae7d74",
            "vehicle_attribute_id": "a14de43925ef48dc922d8ae1a5100075",
            "year": "2025"
        }
    ]
}
