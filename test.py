from dotenv import load_dotenv
import os
from flask_sqlalchemy import SQLAlchemy

# Load environment variables from .env
load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_PORT = os.getenv("DB_PORT")

print(DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME)