import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="TOM",
        password="TOM",
        database="school_db"
    )