# This code will read the contents of a file and print it
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# This code will add to the contents of a file
with open("my_file.txt", mode="a") as file:
    file.write("\n I am male.")


# This code will replace the contents of a file
with open("my_file.txt", mode="w") as file:
    file.write("My name is Angie.\nI am female.")


# This code will create a new file called new_file.txt
with open("new_file.txt", mode="w") as new_file:
    new_file.write("This is just another new file.")


