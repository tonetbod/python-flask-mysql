# import mysql.connector

# def get_connection():
#     return mysql.connector.connect(
#         host="localhost",
#         user="TOM",
#         password="TOM",
#         database="school_db"
#     )


import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "TOM"),
        password=os.getenv("DB_PASSWORD", "TOM"),
        database=os.getenv("DB_NAME", "school_db"),
        port=int(os.getenv("DB_PORT", "3306"))
    )