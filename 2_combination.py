import json


def create():
    students = {}
    with open("2.txt", "w") as f:
        n = int(input("Enter number of students: "))
        for _ in range(n):
            s_id = int(input("Enter student ID:"))
            s_name = input("Enter student name: ")
            grade = int(input("Enter grade: "))
            comb = input("Enter combination: ")
            students[s_id] = [s_name, grade, comb]
        json.dump(students, f)


def read():
    with open("2.txt", "r") as f:
        file = json.load(f)
        print(file)
        comb = input("enter the combination to be searched: ")
        for students in file.values():
            if students[2] == comb:
                print(students[0])


create()
read()
