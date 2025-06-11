from conn_config import config

db_name = input("Enter the name of the DB you want to create")

# 1. Connect to MySQL
conn = config()
cursor = conn.cursor()

# 2. Create database if not exists (optional)
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
cursor.execute(f"USE {db_name}")
