import smtplib

my_email = "ondurufelix1@yahoo.com"
password = "wxjsfbvuvozykifq"
# Sets up the connection with SMTP Information
with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
    # Makes the connection secure
    connection.starttls()

    # Login using username and password
    connection.login(user=my_email, password=password)

    # Sending the email with subject and message
    connection.sendmail(from_addr=my_email,
                        to_addrs="pythonsmtp404@gmail.com",
                        msg="Subject:HELLO\n\nThis is the body."
                        )
