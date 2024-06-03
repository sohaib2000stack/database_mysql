import mysql.connector
from mysql.connector import Error

def get_db_connection():
    try:
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="test2"
        )
        return mydb
    except Error as err:
        raise Exception(f"Error connecting to database: {err}")
