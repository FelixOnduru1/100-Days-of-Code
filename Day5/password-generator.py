import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
           'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
           'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '*', '(', ')', '+']
print("Welcome to the Password Generator!")
num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like in your password?\n"))
num_numbers = int(input("How many numbers would you like in your password?\n"))

password_list = []
# Create a random list of numbers
for i in range(1, num_letters + 1):
    password_list.append(random.choice(letters))
for i in range(1, num_numbers + 1):
    password_list.append(random.choice(numbers))
for i in range(1, num_symbols + 1):
    password_list.append(random.choice(symbols))
random.shuffle(password_list)
password = ''.join(password_list)
print(f"Your password is {password}")
