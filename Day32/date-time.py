import datetime as dt

now = dt.datetime.now()

# To get the attributes of the datetime
print(now.year)
print(now.month)
print(now.weekday())

# Creating datetime from scratch
date_of_birth = dt.datetime(year=1998, month=10, day=25)
print(date_of_birth)

