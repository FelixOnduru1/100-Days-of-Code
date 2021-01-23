import random

test_seed = int(input("Create a seed number:\n"))
random.seed(test_seed)
namesAsCSV = input("Give me the names of people on the table, separating each name with a comma:\n")
names = namesAsCSV.split(", ")
random_index = random.randint(0, (len(names) - 1))

print(f"The person that will pay bill is {names[random_index]}.")
