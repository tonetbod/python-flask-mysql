# import mysql.connector


# def get_connection():

#     return mysql.connector.connect(
#         host="localhost",
#         user="TOM",
#         password="TOM",  # Enter your MySQL password
#         database="restschool",
#         port=3306
#     )


# if __name__ == "__main__":

#     try:
#         conn = get_connection()

#         print("REST School Database Connected Successfully!")

#         conn.close()

#     except mysql.connector.Error as error:

#         print("Database Connection Failed:", error)


import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "TOM"),
        password=os.getenv("DB_PASSWORD", "TOM"),
        database=os.getenv("REST_DB_NAME", "restschool"),
        port=int(os.getenv("DB_PORT", "3306"))
    )


if __name__ == "__main__":
    try:
        conn = get_connection()
        print("REST School Database Connected Successfully!")
        conn.close()

    except mysql.connector.Error as error:
        print("Database Connection Failed:", error)