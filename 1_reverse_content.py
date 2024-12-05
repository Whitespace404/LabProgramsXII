# Python program to Reverse the content in the text file line by line

with open("1.txt", "r") as f:
    lines = [s.rstrip() for s in f.readlines()]

    reversed_lines = []
    for line in lines:
        reversed_lines.append(line[::-1] + "\n")

with open("1.txt", "w") as f:
    f.writelines(reversed_lines)
