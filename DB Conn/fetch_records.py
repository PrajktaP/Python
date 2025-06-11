import sys
from conn_config import config

# db_name = input("Enter the name of the DB you want to fetch records from: ")
if(len(sys.argv) != 3):
    print("Invalid arguments")
    exit()
db_name = sys.argv[1]

# 1. Connect to MySQL
conn = config()
cursor = conn.cursor()

cursor.execute(f"USE {db_name}")

# 3. Fetch records
table_name = sys.argv[2]
cursor.execute(f"SELECT * FROM {table_name}")

results = cursor.fetchall()  # Gets all results
for row in results:
    print(type(row))
    print(row)

