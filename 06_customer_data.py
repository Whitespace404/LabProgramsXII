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
    with open("07.dat", "wb") as file:
        pickle.dump(input_dictionary(), file)


def read():
    with open("07.dat", "rb") as file:
        d = pickle.load(file)
        print(d)


def menu_driver():
    choice = 0
    while choice != 3:
        print(
            """
1: Create a new binary file
2: Read file
3: Exit
    """
        )
        choice = int(input("> "))

        if choice == 1:
            create()
        elif choice == 2:
            read()


menu_driver()
