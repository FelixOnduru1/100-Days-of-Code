from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import os
import time

EMAIL = os.environ["EMAIL"]
TINDER_URL = "https://tinder.com/"
FACEBOOK_PASSWORD = os.environ["FACEBOOK_PASSWORD"]
chrome_driver_path = "C:/Users/WORLDCOLE/Documents/DEVELOPMENT/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(TINDER_URL)

time.sleep(5)
log_in = driver.find_element_by_xpath("//*[@id='t-690321948']/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button")
log_in.click()

time.sleep(10)
facebook_log_in = driver.find_element_by_xpath('//*[@id="t--1349883856"]/div/div/div[1]/div/div[3]/span/div[2]/button')
facebook_log_in.click()

time.sleep(5)
facebook_log_in_window = driver.window_handles[1]
driver.switch_to.window(facebook_log_in_window)
print(driver.title)

time.sleep(5)
email_input = driver.find_element_by_id("email")
email_input.send_keys(EMAIL)

password_input = driver.find_element_by_id("pass")
password_input.send_keys(FACEBOOK_PASSWORD)

facebook_log_in_button = driver.find_element_by_id("loginbutton")
facebook_log_in_button.click()

time.sleep(5)
tinder_page = driver.window_handles[0]
driver.switch_to.window(tinder_page)

time.sleep(5)
allow_location_button = driver.find_element_by_xpath('//*[@id="t--1349883856"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()

time.sleep(5)
not_interested_button = driver.find_element_by_xpath('//*[@id="t--1349883856"]/div/div/div/div/div[3]/button[2]')
not_interested_button.click()

time.sleep(5)
allow_cookies_button = driver.find_element_by_xpath('//*[@id="t-690321948"]/div/div[2]/div/div/div[1]/button')
allow_cookies_button.click()

time.sleep(5)
no_thanks_button = driver.find_element_by_xpath('//*[@id="t--1349883856"]/div/div/div[1]/button')
no_thanks_button.click()


swipe_right = driver.find_element_by_xpath('//*[@id="t-690321948"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[4]/button')

swipe_left = driver.find_element_by_xpath('//*[@id="t-690321948"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[2]/button')


for n in range(100):
    time.sleep(5)

    try:
        swipe_right.click()

    # When there is a match
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()
        except NoSuchElementException:
            time.sleep(5)

driver.close()
