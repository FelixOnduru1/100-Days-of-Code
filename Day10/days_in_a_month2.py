def is_leap(year):
    if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0 and year % 400 != 0:
        return True
    else:
        return False


def days_in_a_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if 1 > month > 12:
        return "Invalid Month"
    if is_leap(year) is True and month == 2:
        return 29
    else:
        return month_days[month - 1]


month_names = ["January", "February", "March", "April", "May", "June",
               "July", "August", "September", "October", "November", "December"]
year_input = int(input("Enter the year:\n"))
month_input = int(input("Enter the month:\n"))
days = days_in_a_month(year=year_input, month=month_input)
print(f"{month_names[month_input - 1]} {year_input} has {days} days.")
