arr = [1, 5, 6, 9, 13, 18]
print(arr)


def create_stack():
    stack = []
    for a in arr:
        if a % 2 == 0:
            stack.append(a * 2)
        else:
            stack.append(a * 5)
    return stack


def pop_stack(stack):
    stack.pop()
    return stack


stack = create_stack()
pop_stack(stack)
print(stack)
