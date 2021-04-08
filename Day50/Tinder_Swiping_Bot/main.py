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

time.sleep(10)
log_in = driver.find_element_by_xpath('//*[@id="t-1147506855"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button')
log_in.click()

time.sleep(10)
facebook_log_in = driver.find_element_by_xpath('//*[@id="t--892698949"]/div/div/div[1]/div/div[3]/span/div[2]/button')
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
allow_location_button = driver.find_element_by_xpath('//*[@id="t--892698949"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()

time.sleep(5)
not_interested_button = driver.find_element_by_xpath('//*[@id="t--892698949"]/div/div/div/div/div[3]/button[2]')
not_interested_button.click()

time.sleep(5)
allow_cookies_button = driver.find_element_by_xpath('//*[@id="t-1147506855"]/div/div[2]/div/div/div[1]/button')
allow_cookies_button.click()

time.sleep(5)
no_thanks_button = driver.find_element_by_xpath('//*[@id="t--892698949"]/div/div/div[1]/button')
no_thanks_button.click()


swipe_right = driver.find_element_by_xpath('//*[@id="t-1147506855"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[4]/button')

swipe_left = driver.find_element_by_xpath('//*[@id="t-1147506855"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[2]/button')


match = 0
for n in range(20):
    time.sleep(5)

    try:
        swipe_right.click()

    # When there is a pop-up
    except ElementClickInterceptedException:
        # Closing add to home screen pop up
        try:
            extra_pop_up = driver.find_element_by_xpath('//*[@id="t--892698949"]/div/div/div[2]/button[2]')
            extra_pop_up.click()

        except NoSuchElementException:

            try:
                # Closing a super like pop up
                super_like_exit = driver.find_element_by_xpath('//*[@id="t--892698949"]/div/div/button[2]')
                super_like_exit.click()
            except NoSuchElementException:

                # Closing a match pop up
                time.sleep(2)
                print("You have a match!")
                match += 1
                match_popup_close = driver.find_element_by_xpath('//*[@id="t--1495887802"]/div/div/div[1]/div/div[4]/button')
                match_popup_close.click()


driver.close()

if match == 1:

    print(f"You have {match} match today.")

else:
    print(f"You have {match} matches today.")