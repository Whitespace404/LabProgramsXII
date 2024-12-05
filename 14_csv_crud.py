import csv


def Update():
    with open("14.csv", "a", newline="\n") as file:
        writer = csv.writer(file)
        ch = ""
        while ch != "y":
            Iid = input("Enter item ID: ")
            name = input("Enter name: ")
            cost = input("Enter cost: ")
            ch = input("Exit? (y/n)?")
            record = [Iid, name, cost]
            writer.writerow(record)


def Display():
    with open("14.csv", "r") as file:
        reader = list(csv.reader(file))
        print(reader)


Update()
Display()
