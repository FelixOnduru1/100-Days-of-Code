print("Welcome to your Pizza Order program.")
pizza_size = input("What is the size of the pizza you want to order? Small, Medium or Large?\n")
bill = 0

if pizza_size == "Small":
    bill += 15
    print(f"Your Pizza({pizza_size}) costs ${bill}.")
elif pizza_size == "Medium":
    bill += 20
    print(f"Your Pizza({pizza_size}) costs ${bill}.")
elif pizza_size == "Large":
    bill += 25
    print(f"Your Pizza({pizza_size}) costs ${bill}")
pepperoni = input("Do you want pepperoni? Yes or No?\n")
if pepperoni == "Yes":
    if pizza_size == "Small":
        bill += 2
        print(f"Your Pepperoni Pizza({pizza_size}) costs ${bill}.")
    else:
        bill += 3
        print(f"Your Pepperoni Pizza({pizza_size}) costs ${bill}.")
    cheese = input("Do you want extra cheese? Yes or No?\n")
    if cheese == "Yes":
        bill += 1
        print(f"Your Pepperoni Pizza({pizza_size}) with extra cheese costs ${bill}.")
    else:
        bill += 0
        print(f"Your Pepperoni Pizza({pizza_size}) without extra cheese costs ${bill}.")
else:
    bill += 0
    print(f"Your Pizza({pizza_size}) costs ${bill}.")
    cheese = input("Do you want extra cheese? Yes or No?\n")
    if cheese == "Yes":
        bill += 1
        print(f"Your Pizza({pizza_size}) with extra cheese costs ${bill}.")
    else:
        bill += 0
        print(f"Your Pizza({pizza_size}) without extra cheese costs ${bill}.")
