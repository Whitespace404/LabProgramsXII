import pickle


def input_dictionary():
    ch = ""
    dictionary = dict()
    while ch != "n":
        Cid = input("Enter item ID: ")
        name = input("Enter name: ")
        cost = int(input("Enter annual price: "))

        dictionary[Cid] = [name, cost]

        ch = input("Would you like to add another? (y/n) ")

    return dictionary


def create():
    with open("10.dat", "wb") as file:
        pickle.dump(input_dictionary(), file)


def read():
    with open("10.dat", "rb") as file:
        d = pickle.load(file)
        for sl, info in d.items():
            if info[1] <= 10000:
                d.pop(sl)
                break
        print(d)
    with open("10.dat", "wb") as file:
        pickle.dump(d, file)


create()
read()
