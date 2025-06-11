from conn_config import config

# 1. Connect to MySQL
conn = config()
cursor = conn.cursor()

db_name = input("Enter the name of the DB you want to fetch records from: ")
cursor.execute(f"USE {db_name}")

# 3. Fetch records
cursor.execute("SELECT * FROM employees")

results = cursor.fetchall()  # Gets all results
for row in results:
    print(type(row))
    print(row)

