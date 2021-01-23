import random
# Generates a random integer between 1 and 10 inclusive
random_integer = random.randint(1, 10)
print(random_integer)

# Generates a random float number between 0 and 0.999999
random_float = random.random()
print(random_float)

# Generates a random float number between 0 and 10, 10 not included.
random_float10 = random.random()*10
print(random_float10)
