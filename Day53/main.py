import os
import time
import requests
from selenium import webdriver
from bs4 import BeautifulSoup


GOOGLE_FORM_LINK = os.environ["GOOGLE_FORM_LINK"]
ZILLOW_URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"

zillow_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0",
    "Accept-Language": "en-CA,en-US;q=0.7,en;q=0.3"
}
zillow_contents = requests.get(url=ZILLOW_URL, headers=zillow_headers).text

soup = BeautifulSoup(zillow_contents, "html.parser")
links = soup.select(selector=".list-card-info .list-card-link")
addresses = soup.find_all(name="address", class_="list-card-addr")
prices = soup.find_all(name="div", class_="list-card-price")


apartment_links = []
for link in links:
    apartment_link = link.get("href")
    if "https" in apartment_link:
        apartment_links.append(apartment_link)

    else:
        apartment_link = "https://www.zillow.com" + apartment_link
        apartment_links.append(apartment_link)


apartment_prices = []
for price in prices:
    apartment_price = price.getText()
    if "+" in apartment_price:
        apartment_prices.append(apartment_price.split("+")[0])
    elif "/" in apartment_price:
        apartment_prices.append(apartment_price.split("/")[0])


apartment_addresses = []
for address in addresses:
    apartment_address = address.getText()
    if "|" in apartment_address:
        apartment_addresses.append(apartment_address.split("|")[1].strip())
    else:
        apartment_addresses.append(apartment_address)


chrome_driver_path = "C:/Users/WORLDCOLE/Documents/DEVELOPMENT/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url=GOOGLE_FORM_LINK)

time.sleep(10)
for n in range(len(apartment_addresses)):
    apartment_address_input = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    apartment_address_input.send_keys(apartment_addresses[n])

    apartment_price_input = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    apartment_price_input.send_keys(apartment_prices[n])

    apartment_link_input = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    apartment_link_input.send_keys(apartment_links[n])

    time.sleep(5)
    submit = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
    submit.click()

    time.sleep(5)
    submit_another_response = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    submit_another_response.click()

driver.close()

