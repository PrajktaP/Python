import sys
from conn_config import config

# db_name = input("Enter the name of the DB you want to create table into: ")
# DB name will be second argument
if(len(sys.argv) != 4):
    print("Invalid arguments")
    exit()
db_name = sys.argv[1]

# 1. Connect to MySQL
conn = config()
cursor = conn.cursor()

# 2. point to the required DB
cursor.execute(f"USE {db_name}")

# 3. table name will be third argument
table_name = sys.argv[2]

# 4. find the list of columns from the respective table
columns_qry = f"""SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS 
WHERE TABLE_NAME = '{table_name}' 
AND COLUMN_NAME != 'id' 
AND TABLE_SCHEMA = '{db_name}';"""

print(columns_qry)
cursor.execute(columns_qry)
columns = cursor.fetchall()  # This gets the results like [('name',), ('age',), ('marks',)]

clms = []
for col in columns:
    clms.append(col[0])  # col is a tuple like ('name',)
print(clms)

# 5. number of the records to be entered will be 4th argument
records_count = int(sys.argv[3])

# 6. gather the data to be used in SQL query
data = []
for i in range(records_count):
    print(f"Record {i+1}")
    single_data = []
    for j in range(len(clms)):
        j = input(f"Enter {clms[j]}: ")
        single_data.append(j)

    data.append(single_data)

print(data)

# 7. insert into DB
insert_query = f"INSERT INTO {table_name} (name, age, marks) VALUES (%s, %s, %s)"
cursor.executemany(insert_query, data)
conn.commit()