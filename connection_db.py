import mysql.connector
from mysql.connector import Error

def create_connection(host_name,user_name, user_password, db_name, port):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            password = user_password,
            database = db_name,
            port = port
        )
        print("Connected")
    except Error as e:
        print(f"Error: {e}")
    return connection


    



