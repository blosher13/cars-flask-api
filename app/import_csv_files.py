import pandas as pd
from db import init_db, db_cursor

# Initialize the database and connection pool
init_db()

df_toyota_details = pd.read_csv("toyota_details.csv")
df_toyota_make_model = pd.read_csv("toyota_make_model.csv")

car_id_map = {}

for _, row in df_toyota_make_model.iterrows():
    with db_cursor() as cursor:
        cursor.execute(
        'INSERT INTO cars (make, model) VALUES (%s, %s)',
        (row["make"], row["model"])
        )
        car_id_map[(row["make"], row["model"])] = cursor.lastrowid  # map to generated ID
cursor.close()

print("Make & Model CSV imported successfully!")

print("Car ID mapping:", car_id_map)

for _, row in df_toyota_details.iterrows():
    car_key = (row["make"], row["model"])
    car_id = car_id_map.get(car_key)
    if not car_id:
       raise ValueError(f"No car_id found for {car_key}")

    with db_cursor() as cursor:
        cursor.execute(
            'INSERT INTO car_attributes (car_id, year, trim, MSRP_price, as_of_datetime) VALUES (%s, %s, %s, %s, %s)',
            (
                car_id, 
                None if pd.isna(row["year"]) else row["year"], 
                None if pd.isna(row["trim"]) else row['trim'], 
                None if pd.isna(row["msrp_price"]) else row['msrp_price'], 
                None if pd.isna(row['as_of_datetime']) else row['as_of_datetime']
                )
        )
cursor.close()

print("Model Details CSV imported successfully!")