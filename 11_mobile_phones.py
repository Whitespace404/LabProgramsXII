import csv


def AddRecord():
    model_no = input("Enter model number: ")
    mobile_name = input("Enter mobile name: ")
    manufacturer = input("Enter manufacturer: ")
    price = input("Enter price: ")

    record = [model_no, mobile_name, manufacturer, price]

    with open("11.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(record)


def Find():
    with open("11.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[2] == "Apple":
                print(row)


AddRecord()
Find()
