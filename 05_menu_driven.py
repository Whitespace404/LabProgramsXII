def create():
    with open("5.txt", "w") as f:
        while True:
            line = input("Enter line: ")
            f.write(line + "\n")
            ch = input("Continue (y/n)? ")
            if ch == "n":
                break


def read():
    with open("5.txt", "r") as f:
        print(f.read())


def digits():
    with open("5.txt", "r") as f:
        digits = [int(i) for i in f.read() if i.isdigit()]
        sum_ = sum(digits)
        average = sum_ / len(digits)
        print(f"There are {len(digits)} digits in the file")
        print(f"Their sum is {sum_}")
        print(f"Their average is {average}")


def lines():
    with open("5.txt", "r") as f:
        n_lines = len(f.readlines())
    print(f"There are {n_lines} lines in the file")


def words():
    with open("5.txt", "r") as f:
        words = f.read().split(" ")
    print(f"There are {len(words)} words in the file.")


def menu_driver():
    choice = 0
    while choice != 6:
        print(
            """
1: Create a new text file
2: Count the number of digits in the file, and their sum and average
3: Find the number of lines in the file
4: Find the number of words in the file
5: Show the contents of the file
6: Exit
    """
        )
        choice = int(input("> "))

        if choice == 1:
            create()
        elif choice == 2:
            digits()
        elif choice == 3:
            lines()
        elif choice == 4:
            words()
        elif choice == 5:
            read()


menu_driver()
