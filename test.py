# test_db.py
from db import init_db, get_connection

# Step 1: Initialize DB (creates database, tables, and connection pool)
init_db()

# Step 2: Test an insert & select
try:
    conn = get_connection()
    cursor = conn.cursor()

    # Insert a sample car
    cursor.execute(
        "INSERT INTO cars (make, model) VALUES (%s, %s)",
        ("Toyota", "Highlander")
    )
    conn.commit()

    print("✅ Inserted sample data successfully!")

    # Read data back
    cursor.execute("SELECT * FROM cars")
    rows = cursor.fetchall()

    print("🚗 Cars in database:")
    for row in rows:
        print(row)

except Exception as e:
    print(f"❌ Error during DB test: {e}")

finally:
    cursor.close()
    conn.close()
