print("Welcome to the FizzBuzz Game!")
user_range = int(input("Input the range of the game:\n"))
for number in range(1, user_range+1):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
