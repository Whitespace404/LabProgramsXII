import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",  # tiger
    database="power",
)
cursor = mydb.cursor()


def create():
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS employees (Eid INT PRIMARY KEY, Ename VARCHAR(255), Salary INT)"
    )
    mydb.commit()
    print("Success.")


def add():
    eid = int(input("Enter employee ID: "))
    ename = input("Enter employee name: ")
    salary = int(input("Enter employee salary: "))

    cursor.execute(
        f'INSERT INTO employees (Eid, Ename, Salary) VALUES ({eid}, "{ename}", {salary})'
    )
    mydb.commit()
    print("Sucess")


def update():
    eid = input("Enter the ID you want to update: ")
    ch = input("Would you like to change the salary (S) or the name (N)? ")

    if ch == "S":
        sal = input("Enter new salary: ")
        cursor.execute(
            "UPDATE employees SET Salary = {} WHERE Eid = {}".format(sal, eid)
        )
        mydb.commit()
        print("Sucess")

    elif ch == "N":
        name = input("Enter new name: ")
        cursor.execute(
            "UPDATE employees SET Ename = '{}' WHERE Eid = {}".format(name, eid)
        )
        mydb.commit()
        print("Sucess")


def delete():
    eid = input("Enter the ID you want to delete: ")
    cursor.execute("DELETE FROM employees WHERE Eid = {}".format(eid))
    mydb.commit()
    print("Sucess")

    pass


def search():
    eid = int(input("Enter the ID you want to search: "))
    cursor.execute("SELECT * FROM employees WHERE Eid = {}".format(eid))
    result = cursor.fetchone()
    print("Employee id:", result[0])
    print("Employee name:", result[1])
    print("Employee salary:", result[2])


def menu_driver():
    choice = 0
    while choice != 6:
        print(
            """
1: Create employee table
2: Add a record
3: Update record
4: Delete record
5: Search
6: Exit
    """
        )
        choice = int(input("> "))

        if choice == 1:
            create()
        elif choice == 2:
            add()
        elif choice == 3:
            update()
        elif choice == 4:
            delete()
        elif choice == 5:
            search()


menu_driver()

cursor.close()
mydb.close()
