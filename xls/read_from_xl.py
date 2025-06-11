import pandas as pd
from conn_config import config

# 1. connect to DB, select the desired DB
conn = config()
cursor = conn.cursor()
cursor.execute(f"USE school")

# 2. read from excel and form the data to be inserted into students table
df = pd.read_excel("students.xlsx", header=None, names=["Name", "Age", "Marks"])
data = []
for index, row in df.iterrows():
    name = row['Name']
    age = row['Age']
    marks = row['Marks']

    # Check if name already exists (case-insensitive match)
    cursor.execute("SELECT 1 FROM students WHERE LOWER(name) = LOWER(%s)", (name,))
    exists = cursor.fetchone()

    # if name matching record is found, do not insert
    if not exists:
        data.append([name, age, marks])

print(data)

# 3. insert into DB
insert_query = "INSERT INTO students (name, age, marks) VALUES (%s, %s, %s)"
cursor.executemany(insert_query, data)
conn.commit()
conn.close()

# # Read Excel file (Sheet1 by default)
# df = pd.read_excel("students.xlsx")  # replace with your file name
# Read Excel file without headers
# df = pd.read_excel("students.xlsx", header=None)