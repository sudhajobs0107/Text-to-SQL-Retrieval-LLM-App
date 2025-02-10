import sqlite3

## Connect to sqlite
connection=sqlite3.connect("student.db")

## Create a cursor object to insert record,create table,retrieve
cursor=connection.cursor()

## create the table
table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT);

"""

cursor.execute(table_info)

## Insert Some more records

cursor.execute('''INSERT INTO STUDENT VALUES ('Mudit', 'Data Science', 'A',95)''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Ankur', 'Data Science', 'B',82)''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Yash', 'Devops', 'C',60)''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Sudha', 'Data Science', 'C',85)''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Mohammad', 'Data Science', 'C',65)''')
  
# Display all the records 
print("The inserted records are:- ") 

data=cursor.execute('''SELECT * FROM STUDENT''') 

for row in data: 
    print(row) 
  
# Closing the connection 

connection.commit() 
connection.close()