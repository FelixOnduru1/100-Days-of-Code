def number_switcher(a, b):
    c = a
    a = b
    b = c
    print("a: " + str(a))
    print("b: " + str(b))


print("Welcome to the two-number switcher. It switches the values of two numbers.")
x = input("What is the a value?\n")
y = input("What is the b value?\n")
number_switcher(x, y)
