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

# Nesting a list in a dictionary
inventory = {
    "stationary": ["pencils", "rubber", "ink"],
    "uniform": ["track suit", "tie", "blazer"],
    "textbooks": ["chemistry", "maths", "grammar"],
}
print(inventory)

# Nesting a dictionary inside a dictionary
inventory_bought = {
    "stationary": {"bought": ["pens", "files"], "amount spent": 100},
    "uniform": {"bought": ["shirts", "socks"], "amount spent": 1500},
    "textbooks": {"bought": ["physics", "biology"], "amount spent": 1000}
}

print(inventory_bought)

# Nesting a dictionary inside a list
inventory_bought_list = [
    {
        "item": "stationary",
        "bought": ["pens", "files"],
        "amount spent": 100
     },
    {
        "item": "uniform",
        "bought": ["shirts", "socks"],
        "amount spent": 1500
     },
    {
        "item": "textbooks",
        "bought": ["physics", "biology"],
        "amount spent": 1000
     },
]
print(inventory_bought_list)


def add_item(new_item, new_bought, new_amount):
    new_dict = {"item": new_item, "bought": new_bought, "amount spent": new_amount}
    inventory_bought_list.append(new_dict)


add_item(new_item="shopping", new_bought=["lamp", "fridge"], new_amount=2000)
print(inventory_bought_list)
