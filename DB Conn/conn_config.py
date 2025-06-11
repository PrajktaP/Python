import mysql.connector

def config():
    conn = mysql.connector.connect(
        host="localhost",      # or your MySQL server IP
        user="root",           # your MySQL username
        password="root",  # your MySQL password
    )
    return conn