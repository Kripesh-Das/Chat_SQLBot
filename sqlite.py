import sqlite3

# Connect to sqlite
connection = sqlite3.connect("student.db")

# Create a cursor object to insert record, create table
cursor = connection.cursor()

# Create the STUD table
table_info = """
CREATE TABLE STUD (
    NAME VARCHAR(25),
    CLASS VARCHAR(25),
    SECTION VARCHAR(25),
    MARKS INT
)
"""

cursor.execute(table_info)

# Insert some more records into STUD table
cursor.execute("INSERT INTO STUD VALUES ('Krish', 'Data Science', 'A', 90)")
cursor.execute("INSERT INTO STUD VALUES ('John', 'Data Science', 'B', 100)")
cursor.execute("INSERT INTO STUD VALUES ('Mukesh', 'Data Science', 'A', 86)")
cursor.execute("INSERT INTO STUD VALUES ('Jacob', 'DEVOPS', 'A', 50)")
cursor.execute("INSERT INTO STUD VALUES ('Dipesh', 'DEVOPS', 'A', 35)")

# Display all the records from STUD table
print("The inserted records are:")
data = cursor.execute("SELECT * FROM STUD")
for row in data:
    print(row)

# Commit your changes in the database
connection.commit()
connection.close()