def add(*args):
    return sum(args)
def subtract(*args):
    first = args[0]
    for i in args[1:]:
        first -= i
    return first
def multiply(*args):
    first = args[0]
    for i in args[1:]:
        first *= i
    return first
def divide(*args):
    first = args[0]
    for i in args[1:]:
        first /= i
    return first