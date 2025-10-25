import mysql.connector
from mysql.connector import pooling, errorcode
from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
DB_PORT = int(os.getenv("DB_PORT", 3306))

from contextlib import contextmanager

def create_database_if_not_exists():
    """Create the database if it doesn't exist yet."""
    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        port=DB_PORT
    )
    cursor = conn.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
    print(f"✅ Database '{DB_NAME}' ready.")
    cursor.close()
    conn.close()

def create_tables_if_not_exists():
    """Create required tables if they don't exist."""
    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        port=DB_PORT
    )
    cursor = conn.cursor()

    # Define your schema here
    TABLES = {}
    TABLES["cars"] = """
        CREATE TABLE IF NOT EXISTS cars (
            car_id INT AUTO_INCREMENT PRIMARY KEY,
            make VARCHAR(50) NOT NULL,
            model VARCHAR(50) NOT NULL
        )
    """
    TABLES["car_attributes"] = """
        CREATE TABLE IF NOT EXISTS car_attributes (
            car_attribute_id INT AUTO_INCREMENT PRIMARY KEY,
            car_id INT,
            year VARCHAR(50) NOT NULL,
            MSRP_price DECIMAL(10,2) NOT NULL,
            FOREIGN KEY (car_id) REFERENCES cars(car_id) ON DELETE CASCADE
        )
    """

    for name, ddl in TABLES.items():
        try:
            cursor.execute(ddl)
            print(f"✅ Table '{name}' ready.")
        except mysql.connector.Error as err:
            print(f"❌ Error creating table {name}: {err}")

    cursor.close()
    conn.close()

# Create a connection pool after tables are ready
def create_connection_pool():
    return pooling.MySQLConnectionPool(
        pool_name="mypool",
        pool_size=5,
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        port=DB_PORT
    )

# Public function to initialize the DB on app startup
def init_db():
    create_database_if_not_exists()
    create_tables_if_not_exists()
    global connection_pool
    connection_pool = create_connection_pool()

def get_connection():
    return connection_pool.get_connection()

@contextmanager
def db_cursor():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        yield cursor
        conn.commit()
    finally:
        cursor.close()
        conn.close()