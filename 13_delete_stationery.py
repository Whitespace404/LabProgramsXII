import csv


def Add_Item():
    with open("13.csv", "a", newline="\n") as file:
        writer = csv.writer(file)
        ch = ""
        while ch != "y":
            Iid = input("Enter item ID: ")
            name = input("Enter name: ")
            cost = input("Enter cost: ")
            ch = input("Exit? (y/n)?")
            record = [Iid, name, cost]
            writer.writerow(record)


def Delete():
    id = input("Enter item_id of the product you want to delete: ")
    with open("13.csv", "r") as f:
        reader = csv.reader(f)
        nr = []
        for read in reader:
            if read[0] != id:
                nr.append(read)
        print(nr)

    with open("13.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(nr)


Delete()
