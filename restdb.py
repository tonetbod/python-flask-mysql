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
from urllib.parse import urlparse, unquote

def get_connection():
    url = urlparse(os.getenv("REST_DATABASE_URL"))

    return mysql.connector.connect(
        host=url.hostname,
        port=url.port or 4000,
        user=unquote(url.username),
        password=unquote(url.password),
        database=url.path.lstrip("/"),
        ssl_verify_cert=True,
        ssl_verify_identity=True
    )

if __name__ == "__main__":
    try:
        conn = get_connection()
        print("REST School Database Connected Successfully!")
        conn.close()

    except mysql.connector.Error as error:
        print("Database Connection Failed:", error)