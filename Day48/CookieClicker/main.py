from selenium import webdriver
import time
from threading import Timer

chrome_driver_path = "C:/Users/WORLDCOLE/Documents/DEVELOPMENT/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(url="http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element_by_id("cookie")

store_items = driver.find_elements_by_css_selector("#store div")
store_items_ids = [store_item.get_attribute("id") for store_item in store_items]

timeout = time.time() + 5
five_min = time.time() + 5*60
while True:
    cookie.click()

    if time.time() > timeout:

        store_items_prices = driver.find_elements_by_css_selector("#store b")
        prices = []
        for store_item_price in store_items_prices:
            if store_item_price.text != "":
                price = int(store_item_price.text.split("-")[1].strip().replace(",", ""))
                prices.append(price)

        # Create dictionary of store items and prices
        upgrades = {}
        for n in range(len(prices)):
            upgrades[prices[n]] = store_items_ids[n]

        # Get current cookie count
        money = driver.find_element_by_id("money").text
        if "," in money:
            money = money.replace(",", "")
        cookie_count = int(money)

        # Find upgrades that we can currently afford
        affordable_upgrades = {}
        for cost, item_id in upgrades.items():
            if cookie_count >= cost:
                affordable_upgrades[cost] = item_id

        # Purchase the most expensive affordable upgrade
        highest_affordable_upgrade = max(affordable_upgrades)
        print(highest_affordable_upgrade)

        item_to_purchase_id = affordable_upgrades[highest_affordable_upgrade]

        # Click
        driver.find_element_by_id(item_to_purchase_id).click()

        # Add another 5 seconds until the next check
        timeout = time.time() + 5

    if time.time() > five_min:
        cookies_per_second = driver.find_element_by_id("cps").text
        print(cookies_per_second)
        break
