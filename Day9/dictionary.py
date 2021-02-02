inventory = {
    "stationary": "pencils",
    "uniform": "track suit",
    "textbooks": "chemistry",
}
# Retrieve items from dictionary
print(inventory["stationary"])

# Adding items to dictionary
inventory["furniture"] = "tables"
print(inventory)

# Looping through a python dictionary
for key in inventory:
    print(inventory[key])
