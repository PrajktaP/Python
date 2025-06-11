import sys
from conn_config import config

# db_name = input("Enter the name of the DB you want to create table into: ")
# if(len(sys.argv) != 2):
#     print("Invalid arguments")
#     exit()
db_name = sys.argv[1]

# 1. Connect to MySQL
conn = config()
cursor = conn.cursor()

# 2. Create database if not exists (optional)
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
cursor.execute(f"USE {db_name}")

table_name = sys.argv[2]
column_args = sys.argv[3:] # parse arguments from 3 onwards

# Parse the column definitions
column_definitions = []
for arg in column_args:
    name, datatype = arg.split(":")
    column_definitions.append(f"{name} {datatype.upper()}")  # Use .upper() for SQL standard

columns_sql = ",".join(column_definitions)

# Compose the full CREATE TABLE query
create_table_sql = f"CREATE TABLE IF NOT EXISTS {table_name} (id INT AUTO_INCREMENT PRIMARY KEY,{columns_sql})"

print(create_table_sql)

cursor.execute(create_table_sql)