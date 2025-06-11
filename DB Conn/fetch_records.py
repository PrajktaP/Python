from conn_config import config

# 1. Connect to MySQL
conn = config()
cursor = conn.cursor()

cursor.execute("USE test_python")

# 3. Fetch records
cursor.execute("SELECT * FROM employees")

results = cursor.fetchall()  # Gets all results
for row in results:
    print(type(row))
    print(row)

