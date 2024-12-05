import mysql.connector

# Connect to the MySQL database
mydb = mysql.connector.connect(
    host="localhost", user="", password="tiger", database="mydatabase"
)

mycursor = mydb.cursor()

# Create the employee table
sql = "CREATE TABLE employee (Eid INT AUTO_INCREMENT PRIMARY KEY, Ename VARCHAR(255), Salary INT)"
mycursor.execute(sql)

# Insert a record into the employee table
sql = "INSERT INTO employee (Ename, Salary) VALUES (%s, %s)"
val = ("John Doe", 10000)
mycursor.execute(sql, val)

# Update a record in the employee table
sql = "UPDATE employee SET Ename = %s WHERE Eid = %s"
val = ("Jane Smith", 2)
mycursor.execute(sql, val)

# Delete a record from the employee table
sql = "DELETE FROM employee WHERE Eid = %s"
val = (3,)
mycursor.execute(sql, val)

# Search for a record in the employee table
sql = "SELECT * FROM employee WHERE Eid = %s"
val = (1,)
mycursor.execute(sql, val)

myresult = mycursor.fetchone()

for x in myresult:
    print(x)

# Display all records from the employee table
sql = "SELECT * FROM employee"
mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

mydb.commit()
mycursor.close()
mydb.close()
