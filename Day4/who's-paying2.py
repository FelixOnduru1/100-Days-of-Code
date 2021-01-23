import random

test_seed = int(input("Create a seed number:\n"))
random.seed(test_seed)
namesAsCSV = input("Give me the names of people on the table, separating each name with a comma:\n")
names = namesAsCSV.split(", ")
random_name = random.choice(names)

print(f"{random_name} will pay for the meal today.")
