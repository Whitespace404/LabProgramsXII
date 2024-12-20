import pickle


def input_dictionary():
    ch = ""
    dictionary = dict()
    while ch != "n":
        Cid = input("Enter customer ID: ")
        name = input("Enter customer name: ")
        city = input("Enter city: ")

        dictionary[Cid] = [name, city]

        ch = input("Would you like to add another? (y/n) ")

    return dictionary


def create():
    with open("06.dat", "wb") as file:
        pickle.dump(input_dictionary(), file)


def read():
    with open("06.dat", "rb") as file:
        d = pickle.load(file)
        print(d)


create()
read()
