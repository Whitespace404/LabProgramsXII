import csv


def Add_Item():
    with open("12.csv", "a", newline="\n") as file:
        writer = csv.writer(file)
        ch = ""
        while ch != "y":
            Iid = input("Enter item ID: ")
            name = input("Enter name: ")
            cost = input("Enter cost: ")
            ch = input("Exit? (y/n)?")
            record = [Iid, name, cost]
            writer.writerow(record)


def Count():
    with open("12.csv", "r") as file:
        reader = list(csv.reader(file))
        print(len(reader))


Add_Item()
Count()
