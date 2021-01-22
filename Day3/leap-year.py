print("Welcome to the Leap Year program.\n"
      " This program determines whether a given year is a leap year.")
year = int(input("Enter the year you want to check:\n"))

if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
    print(f"The year {year} is a leap year.")
elif year % 4 == 0 and year % 100 != 0 and year % 400 != 0:
    print(f"The year {year} is a leap year.")
else:
    print(f"The year {year} is not a leap year.")
