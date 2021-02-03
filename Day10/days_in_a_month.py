year_input = int(input("Enter a year:\n"))
month_input = int(input("Enter a month:\n")) - 1


def days_in_a_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leap_year = False
    if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        leap_year = True
    elif year % 4 == 0 and year % 100 != 0 and year % 400 != 0:
        leap_year = True
    else:
        leap_year = False

    if leap_year is True:
        month_days[1] += 1
    num_days = month_days[month]
    print(num_days)


days_in_a_month(year=year_input, month=month_input)
