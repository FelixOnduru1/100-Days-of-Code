from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import os
import time
from datetime import datetime

EMAIL = os.environ["EMAIL"]
TINDER_URL = "https://tinder.com/"
FACEBOOK_PASSWORD = os.environ["FACEBOOK_PASSWORD"]
chrome_driver_path = "C:/Users/WORLDCOLE/Documents/DEVELOPMENT/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(TINDER_URL)

current_time = datetime.now()
actual_time = current_time.strftime("%Y-%m-%d %H-%M-%S")
time.sleep(10)
log_in = driver.find_element_by_xpath(
    '//*[@id="t-1147506855"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button')
log_in.click()

time.sleep(10)
facebook_log_in = driver.find_element_by_xpath('//*[@id="t--892698949"]/div/div/div[1]/div/div[3]/span/div[2]/button')
facebook_log_in.click()

time.sleep(10)
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
allow_cookies_button = driver.find_element_by_xpath('//*[@id="t-1147506855"]/div/div[2]/div/div/div[1]/button')
allow_cookies_button.click()

time.sleep(5)
unable_facebook = driver.find_element_by_xpath('//*[@id="t--892698949"]/div/div/div[1]/div/div[3]/span/div[2]/button')
unable_facebook.click()

time.sleep(5)
allow_location_button = driver.find_element_by_xpath('//*[@id="t--892698949"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()

time.sleep(5)
not_interested_button = driver.find_element_by_xpath('//*[@id="t--892698949"]/div/div/div/div/div[3]/button[2]')
not_interested_button.click()

time.sleep(5)
no_thanks_button = driver.find_element_by_xpath('//*[@id="t--892698949"]/div/div/div[1]/button')
no_thanks_button.click()

swipe_right = driver.find_element_by_xpath(
    '//*[@id="t-1147506855"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[4]/button')

swipe_left = driver.find_element_by_xpath(
    '//*[@id="t-1147506855"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[2]/button')

match = 0
index_of_swipe = []
type_swipe = []
result = []
for n in range(10):
    time.sleep(5)

    try:
        swipe_right.click()
        index_of_swipe.append(n)
        type_swipe.append("swipe")
        result.append(0)

    # When there is a pop-up
    except ElementClickInterceptedException:
        # Closing add to home screen pop up
        try:
            extra_pop_up = driver.find_element_by_xpath('//*[@id="t--892698949"]/div/div/div[2]/button[2]')
            extra_pop_up.click()
            index_of_swipe.append(n)
            type_swipe.append("pop-up")
            print(f"This is index {n}. This is a pop-up.")
            result.append(0)

        except NoSuchElementException:
            index_of_swipe.append(n)

            try:
                # Closing a super like pop up
                super_like_exit = driver.find_element_by_xpath('//*[@id="t--892698949"]/div/div/button[2]')
                super_like_exit.click()
                print(f"This is index {n}. This is a super like.")
                type_swipe.append("pop-up")
            except NoSuchElementException:

                # Closing a match pop up
                time.sleep(2)
                print("You have a match!")
                print(f"This is index {n}. This is a match.")
                index_of_swipe.append(n)
                type_swipe.append("match")
                result.append(1)

                match += 1
                match_popup_close = driver.find_element_by_xpath(
                    '//*[@id="t--1495887802"]/div/div/div[1]/div/div[4]/button')
                match_popup_close.click()

driver.close()

print(type_swipe)

for item in type_swipe:
    if item == "match":
        index = type_swipe.index(item)
        type_swipe[index] = "successful"
        type_swipe.pop(index-1)

    elif item == "pop-up":
        index = type_swipe.index(item)
        type_swipe[index] = "eliminated"
        type_swipe.pop(index)
        type_swipe.pop(index-1)


print(type_swipe)
print(len(type_swipe))
with open(file=f"{actual_time}.txt", mode="w") as file:
    for value in type_swipe:
        file.write(f"{value},\n")


if match == 1:

    print(f"You have {match} match today.")

else:
    print(f"You have {match} matches today.")
