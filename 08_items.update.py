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
    with open("08.dat", "wb") as file:
        pickle.dump(input_dictionary(), file)


def read():
    with open("08.dat", "rb") as file:
        d = pickle.load(file)
        print(d)


def update():
    with open("08.dat", "rb") as file:
        d = pickle.load(file)

    name = input("Enter the name of the item to update: ")

    for Cid in d:
        if d[Cid][0] == name:
            new_cost = int(input("Enter the new cost: "))
            d[Cid][1] = new_cost
            break
    else:
        print("Item not found")

    with open("08.dat", "wb") as file:
        pickle.dump(d, file)


def menu_driver():
    choice = 0
    while choice != 4:
        print(
            """
1: Create a new text file
2: Read text file
3: Update text file
4: Exit
    """
        )
        choice = int(input("> "))

        if choice == 1:
            create()
        elif choice == 2:
            read()
        elif choice == 3:
            update()


menu_driver()
