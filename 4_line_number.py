def create():
    with open("4.txt", "w") as f:
        while True:
            line = input("Enter line: ")
            f.write(line + "\n")
            ch = input("Continue (y/n)? ")
            if ch == "n":
                break


def find_line():
    target = input("What word would you like to search for?")
    with open("4.txt", "r") as f:
        lines = [l.rstrip() for l in f.readlines()]
        for n, line in enumerate(lines, 1):
            if line == target:
                print(f"{target} was found in line {n}")
                break


create()
find_line()
