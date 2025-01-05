D = {"Victorinox Jetsetter": 110, "Victorinox Lite": 20, "Victorinox Rambler": 60}


def stack_push(stack, element):
    stack.append(element)


def stack_pop(stack):
    stack.pop()


stack = []
for name, cost in D.items():
    if cost > 100:
        stack_push(stack, cost)

stack_pop(stack)
print(stack)
