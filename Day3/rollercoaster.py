print("Welcome to the Rollercoaster.\n"
      "This program checks for height and determines whether you can ride or not and the amount to pay.")
height = int(input("What is your height in cm?\n"))
age = int(input("What is your age?\n"))
bill = 0
if height >= 120:
    print("You can ride the Rollercoaster.")
    if age < 12:
        bill += 5
        print(f"Children tickets cost ${bill}.")
    elif 12 <= age <= 18:
        bill += 7
        print(f"Youth tickets cost ${bill}.")
    else:
        bill += 12
        print(f"Adult tickets cost ${bill}.")
    photo_package = input("Do you want a photo taken? Yes or No?\n")
    if photo_package == "Yes":
        bill += 3
        print(f"Your total cost is ${bill}.")
    else:
        bill += 0
        print(f"Your total cost is ${bill}.")
else:
    print(f"Sorry, you can't ride the Rollercoaster! You need to grow {120-height}cm to ride.")
