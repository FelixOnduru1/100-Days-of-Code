import smtplib
import random
import datetime as dt

my_email = "pythonsmtp404@gmail.com"
password = "EAUybinT3Dwespr"

now = dt.datetime.now()
day_of_week = now.weekday()
print(day_of_week)
if day_of_week == 1:
    with open("quotes.txt") as data_file:
        content = data_file.readlines()
        quote = random.choice(content)
        print(quote)

    # Sets up the connection with SMTP Information
    with smtplib.SMTP("smtp.gmail.com") as connection:
        # Makes the connection secure
        connection.starttls()

        # Login using username and password
        connection.login(user=my_email, password=password)

        # Sending the email with subject and message
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"Subject:HAPPY NEW WEEK\n\n{quote}".encode('utf-8')
                            )
