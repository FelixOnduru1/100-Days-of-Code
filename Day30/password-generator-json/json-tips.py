import json

# Reading a json file and turning it into a dictionary
with open("password.json", mode="r") as data_file:
    data = json.load(data_file)
    print(data)
