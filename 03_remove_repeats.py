def create():
    with open("3.txt", "w") as f:
        while True:
            line = input("Enter line: ")
            f.write(line + "\n")
            ch = input("Continue (y/n)? ")
            if ch == "n":
                break


def remove_repeats():
    with open("3.txt", "r") as f:
        print(f.read() + "\n")
        f.seek(0)
        unique_lines = set(f.readlines())
    with open("3.txt", "w") as f:
        f.writelines(unique_lines)
    with open("3.txt", "r") as f:
        print(f.read())


create()
remove_repeats()
