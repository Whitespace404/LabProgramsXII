import pickle


def input_dictionary():
    ch = ""
    dictionary = dict()
    while ch != "n":
        Cid = input("Enter item ID: ")
        name = input("Enter gift name: ")
        cost = int(input("Enter cost: "))

        dictionary[Cid] = [name, cost]

        ch = input("Would you like to add another? (y/n) ")

    return dictionary


def create():
    with open("07.dat", "wb") as file:
        pickle.dump(input_dictionary(), file)


def read():
    with open("07.dat", "rb") as file:
        d = pickle.load(file)
        print(d)


create()
read()
