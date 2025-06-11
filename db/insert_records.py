import sys
from conn_config import config

# db_name = input("Enter the name of the DB you want to create table into: ")
if(len(sys.argv) != 4):
    print("Invalid arguments")
    exit()
db_name = sys.argv[1]

# 1. Connect to MySQL
conn = config()
cursor = conn.cursor()

cursor.execute(f"USE {db_name}")

# get records data from user
# records_count = int(input("Enter how many records you want to insert: "))
records_count = int(sys.argv[3])

data = []
for i in range(records_count):
    name = input("Enter the name: ")
    age = input("Enter age: ")
    marks = input("Enter the marks: ")

    data.append([name, age, marks])

# insert into DB
table_name = sys.argv[2]
insert_query = f"INSERT INTO {table_name} (name, age, marks) VALUES (%s, %s, %s)"
cursor.executemany(insert_query, data)
conn.commit()