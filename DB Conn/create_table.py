from conn_config import config

db_name = input("Enter the name of the DB you want to create table into: ")

# 1. Connect to MySQL
conn = config()
cursor = conn.cursor()

# 2. Create database if not exists (optional)
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
cursor.execute(f"USE {db_name}")


# 3. Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    marks INT(50)
)
""")
