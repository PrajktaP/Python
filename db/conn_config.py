import mysql.connector

def config():
    conn = mysql.connector.connect(
        host="localhost",      # or your MySQL server IP
        user="dljalksdjas",           # your MySQL username
        password="adalksdjaslkd",  # your MySQL password
    )
    return conn