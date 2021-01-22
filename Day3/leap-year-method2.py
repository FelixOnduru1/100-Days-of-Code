print("Welcome to the Leap Year 2 program.\n"
      " This program determines whether a given year is a leap year.")
year = int(input("Enter the year you want to check:\n"))

if year % 4 == 0:
    if year % 100 != 0:
        print(f"The year {year} is a leap year.")
        if year % 400 == 0:
            print(f"The year {year} is a leap year.")
        else:
            print(f"The year {year} is not a leap year.")
    else:
        print(f"The year {year} is not a leap year.")
else:
    print(f"The year {year} is not a leap year.")
