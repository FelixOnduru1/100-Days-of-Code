import smtplib
import random
import datetime as dt
import os

my_email = "pythonsmtp404@gmail.com"
password = os.environ["EMAIL_PASSWORD"]

now = dt.datetime.now()
day_of_week = now.weekday()
print(day_of_week)
if day_of_week == 0:
    with open("quotes.txt") as data_file:
        content = data_file.readlines()
        quote = random.choice(content)
        print(quote)

    # Sets up the connection with SMTP Information
    with smtplib.SMTP("smtp.gmail.com", 587, timeout=120) as connection:
        # Makes the connection secure
        connection.starttls()

        # Login using username and password
        connection.login(user=my_email, password=password)

        # Sending the email with subject and message
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"Subject:HAPPY NEW WEEK\n\n{quote}".encode('utf-8')
                            )
