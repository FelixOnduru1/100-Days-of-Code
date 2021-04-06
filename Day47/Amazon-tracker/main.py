import requests
import lxml
import os
import smtplib
from bs4 import BeautifulSoup
EMAIL = "pythonsmtp404@gmail.com"
PASSWORD = os.environ["EMAIL_PASSWORD"]
AMAZON_URL = "https://www.amazon.com/Canon-RF50mm-Mirrorless-Cameras-4515C002/dp/B08MFVH7SV/ref=sr_1_14?dchild=1&keywords=canon+lens&qid=1617683771&sr=8-14"
amazon_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0",
    "Accept-Language": "en-CA,en-US;q=0.7,en;q=0.3"
}
amazon_website = requests.get(url=AMAZON_URL, headers=amazon_headers)
amazon = amazon_website.content
soup = BeautifulSoup(amazon, "lxml")

product_title = soup.find(id="productTitle").getText().strip()
price = soup.find(name="span", id="priceblock_ourprice").getText()
price_as_float = float(price.split("$")[1])
print(price_as_float)

if price_as_float <= 100:
    with smtplib.SMTP("smtp.gmail.com") as connection:

        connection.starttls()

        connection.login(user=EMAIL, password=PASSWORD)

        connection.sendmail(from_addr=EMAIL,
                            to_addrs=EMAIL,
                            msg=f"Subject:Amazon Price Alert\n\n{product_title}"
                                f" is now ${price_as_float}.\n{AMAZON_URL}".encode('utf-8')
                            )


