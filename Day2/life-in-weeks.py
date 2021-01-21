print("This program tells you tje number of days, weeks and years of your life left")
age = int(input("What is your current age?\n"))
aspiring_age = int(input("How many years do you want to live?\n"))

years_left = aspiring_age - age
months_left = years_left*12
weeks_left = years_left*52
days_left = years_left*365

print(f"You only have {months_left} months left.\nYou only have {weeks_left} weeks left."
      f"\nYou only have {days_left} days left.")
