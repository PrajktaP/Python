from conn_config import config

# 1. Connect to MySQL
conn = config()
cursor = conn.cursor()

db_name = input("Enter the name of the DB you want to insert records into: ")
cursor.execute(f"USE {db_name}")

# get records data from user
records_count = int(input("Enter how many employee records you want to insert: "))

data = []
for i in range(records_count):
    name = input("Enter the name: ")
    age = input("Enter age: ")
    dept = input("Enter the department: ")

    data.append([name, age, dept])

# insert into DB
insert_query = "INSERT INTO employees (name, age, department) VALUES (%s, %s, %s)"
cursor.executemany(insert_query, data)
conn.commit()