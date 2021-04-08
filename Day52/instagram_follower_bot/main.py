from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
import os
import time

INSTAGRAM_USERNAME = os.environ["INSTAGRAM_USERNAME"]
INSTAGRAM_PASSWORD = os.environ["INSTAGRAM_PASSWORD"]
INSTAGRAM_URL = "https://www.instagram.com/"
CHROME_DRIVER_PATH = "C:/Users/WORLDCOLE/Documents/DEVELOPMENT/chromedriver.exe"


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        self.driver.get(url=INSTAGRAM_URL)

    def log_in(self):
        time.sleep(10)
        username_input = self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input')
        username_input.send_keys(INSTAGRAM_USERNAME)

        password_input = self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input')
        password_input.send_keys(INSTAGRAM_PASSWORD)

        log_in_button = self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button')
        log_in_button.click()

        time.sleep(5)
        not_now_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
        not_now_button.click()

        time.sleep(5)
        not_now_notifications_button = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
        not_now_notifications_button.click()

        print("Bot has successfully logged in.")

    def find_followers(self, user, number):
        time.sleep(5)
        search_user = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        search_user.send_keys(user)

        time.sleep(5)
        select_first_user = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a')
        select_first_user.click()

        time.sleep(20)
        followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()

        time.sleep(10)
        pop_up_followers = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')

        for _ in range(number):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", pop_up_followers)

    def follow(self):

        follow_buttons = self.driver.find_elements_by_css_selector("li button")

        for follow_button in follow_buttons:
            try:
                follow_button.click()
                time.sleep(2)

            except ElementClickInterceptedException:
                self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]').click()
                time.sleep(2)

        print("The InstaFollower Bot completed successfully.")


insta_follower_bot = InstaFollower()
insta_follower_bot.log_in()
insta_follower_bot.find_followers(user="python", number=10)
insta_follower_bot.follow()
