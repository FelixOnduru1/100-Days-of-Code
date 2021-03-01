numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers]
print(new_list)

name = "Felix"
letters_list = [letter for letter in name]
print(letters_list)

doubled_num = [2 * n for n in range(1, 11)]
print(doubled_num)

doubled_num_even = [2 * n for n in range(1, 11) if n % 2 == 0]
print(doubled_num_even)
