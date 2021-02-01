print("This program checks if a number is prime or not.")


def prime_number_checker(number):
    is_prime = True
    for i in range(2, number-1):
        if number % i == 0:
            is_prime = False

    if is_prime:
        print(f"The number {number} is prime.")
    else:
        print(f"The number {number} is not prime.")


user_number = int(input("Enter the number you want to check:\n"))
prime_number_checker(number=user_number)
