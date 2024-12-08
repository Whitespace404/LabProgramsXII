# Python program to Reverse the content in the text file line by line

with open("1.txt", "r") as f:
    lines = []
    for line in f.readlines():
        l = line.rstrip()
        lines.append(l)
        print(l)

    print()

    reversed_lines = []
    for line in lines:
        reversed = line[::-1]
        reversed_lines.append(reversed + "\n")
        print(reversed)


with open("1.txt", "w") as f:
    f.writelines(reversed_lines)
