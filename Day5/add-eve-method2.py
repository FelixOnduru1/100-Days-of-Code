user_range = int(input("Input the range you want the even numbers added:\n"))
sum_even = 0
for even in range(2, user_range + 1, 2):
    sum_even += even
print(f"The sum of the even numbers between 1 and {user_range} (100 inclusive) is {sum_even}.")
