import pandas as pd
import datetime as dt
import smtplib
import random

my_email = "pythonsmtp404@gmail.com"
password = "EAUybinT3Dwespr"
# with open("birthdays.csv", mode="a") as data_file:
#     data_file.write("Felix,python404@gmail.com,1998,3,10")

now = dt.datetime.now()
today = (now.month, now.day)


birthdays = pd.read_csv("birthdays.csv").reset_index(drop=True)
birthdays_dict = {(row.month, row.day): row
                  for (index, row) in birthdays.iterrows()}

if today in birthdays_dict:
    name = birthdays_dict[today]["name"]
    to_email = birthdays_dict[today]["email"]
    with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as letter_template:
        letter_content = letter_template.read().replace("[NAME]", f"{name}")

    with smtplib.SMTP("smtp.gmail.com") as connection:

        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=to_email,
                            msg=f"Subject:HAPPY BIRTHDAY!!!\n\n{letter_content}")

# You can use Python Anywhere to schedule the task
