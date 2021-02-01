print("This program checks if a number is prime or not.")
num_entry = int(input("What is the number you want to check?\n"))

if num_entry <= 0:
    print(f"The number {num_entry} is not prime.")
elif num_entry > 2 and num_entry % 2 == 0:
    print(f"The number {num_entry} is not prime.")
elif num_entry > 3 and num_entry % 3 == 0:
    print(f"The number {num_entry} is not prime.")
elif num_entry > 5 and num_entry % 5 == 0:
    print(f"The number {num_entry} is not prime.")
elif num_entry > 7 and num_entry % 7 == 0:
    print(f"The number {num_entry} is not prime.")
elif num_entry > 11 and num_entry % 11 == 0:
    print(f"The number {num_entry} is not prime.")
elif num_entry > 13 and num_entry % 13 == 0:
    print(f"The number {num_entry} is not prime.")
else:
    print(f"The number {num_entry} is prime.")
