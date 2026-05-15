def hello_world():
    print("Hello, World!")


hello_world()

# only small letters and underscores are allowed in function names. anything else is not allowed.


def sum(num1=0, num2=0):
    if type(num1) is not int or type(num2) is not int:
        return "Both parameters must be integers."
    else:
        return num1 + num2


# total = sum("a", 10)
# print(total)


def multiple_items(*args):

    return args


multiple_items("apple", "banana", "orange")
