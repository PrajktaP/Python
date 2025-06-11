import mysql.connector

def config():
    conn = mysql.connector.connect(
        host="localhost",      # or your MySQL server IP
        user="rosldlaksdklot",           # your MySQL username
        password="asjdlasjd",  # your MySQL password
    )
    return conn