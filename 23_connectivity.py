import mysql.connector as mysql

db = mysql.connect(host="localhost", user="root", password="root" # tiger)
cursor = db.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS school")
cursor.execute("USE school")
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS student (
        rollno INT PRIMARY KEY, 
        stname VARCHAR(10)
    )
"""
)


def insert_records():
    n = int(input("How many records would you like to insert?"))
    for _ in range(n):
        rollno = int(input("Enter roll number: "))
        name = input("Enter name: ")

        cursor.execute(
            f'INSERT INTO student (rollno, stname) VALUES ({rollno}, "{name}")'
        )
        db.commit()
        print()
    print("Record inserted.")


def display_records():
    cursor.execute("SELECT * FROM student")
    for record in cursor.fetchall():
        print(record)


def search_record():
    roll = int(input("Enter roll number to search: "))
    cursor.execute("SELECT * FROM student WHERE rollno ={}".format(roll))
    print(cursor.fetchone())


def update_record():
    roll = int(input("Enter roll number to update: "))
    name = input("Enter new name: ")
    cursor.execute(
        "UPDATE student SET stname = '{}' WHERE rollno = {}".format(name, roll)
    )
    db.commit()
    print("Record updated.")


def delete_record():
    roll = int(input("Enter roll number to delete: "))
    cursor.execute("DELETE FROM student WHERE rollno = {}".format(roll))
    db.commit()
    print("Record deleted.")


operations = {
    "1": insert_records,
    "2": display_records,
    "3": search_record,
    "4": update_record,
    "5": delete_record,
}


def menu_driver():
    while True:
        print("\n1. Insert\n2. Display\n3. Search\n4. Update\n5. Delete\n6. Exit")
        choice = int(input("> "))
        if choice == 6:
            break
        elif choice == 1:
            insert_records()
        elif choice == 2:
            display_records()
        elif choice == 3:
            search_record()
        elif choice == 4:
            update_record()
        elif choice == 5:
            delete_record()
        else:
            print("Invalid choice.")


menu_driver()
db.close()
