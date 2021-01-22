print("Welcome to the Rollercoaster.\n"
      "This program checks for height and determines whether you can ride or not and the amount to pay.")
height = int(input("What is your height in cm?\n"))
age = int(input("What is your age?\n"))
if height >= 120:
    print("You can ride the Rollercoaster.")
    if age < 12:
        print("You will pay $5.00 to ride. Enjoy!!")
    elif 12 <= age <= 18:
        print("You will pay $7:00 to ride. Enjoy!!")
    else:
        print("You will pay $12.00 to ride. Enjoy!!")
else:
    print(f"Sorry, you can't ride! You need to grow {120-height}cm to ride.")
