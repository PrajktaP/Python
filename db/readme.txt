> python test_db_conn.py new_db
> python create_table.py new_db table_name "column1:datatype" "column2:datatype" "column3:datatype"
example python create_table.py school students "name:varchar(100)" "age:int" "marks:float"
> python insert_records.py new_db students
> python fetch_records.py new_db students


TODO: 
Acccept table_name and columns through command line in create_table. DONE
Update insert records code to dynamically decide what values to get from user.
or Update insert records to get data from a csv or excel file and then insert into DB.

