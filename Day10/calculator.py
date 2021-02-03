def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1/n2


operations = {"+": add,
              "-": subtract,
              "*": multiply,
              "/": divide
              }


def calculator():

    num1 = float(input("What is the first number?\n"))

    calculator_active = True

    while calculator_active:
        print("Pick an operation below:")
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Enter the operation:\n")
        next_num = float(input("What is the next number?\n"))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(n1=num1, n2=next_num)
        print(f"{num1} {operation_symbol} {next_num} = {answer}")

        calculator_status = input(f"Type 'y' to continue with {answer}, or 'n' to start a new calculation:\n ")

        if calculator_status == "y":
            calculator_active = True
            num1 = answer

        else:
            calculator_active = False
            calculator()


calculator()
