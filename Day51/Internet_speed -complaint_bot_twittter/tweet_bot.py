from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import os

TWITTER_URL = "https://twitter.com/"
TWITTER_EMAIL = os.environ["TWITTER_EMAIL"]
TWITTER_PASSWORD = os.environ["TWITTER_PASSWORD"]


class TweetBot:

    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)

    def tweet(self, tweet):
        self.driver.get(url=TWITTER_URL)
        time.sleep(5)

        # Log in button click
        self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/a[2]').click()

        time.sleep(5)
        # Input email and password
        self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input').send_keys(TWITTER_EMAIL)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input').send_keys(TWITTER_PASSWORD)

        time.sleep(5)
        # Sign-in


        self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div').click()


        time.sleep(5)
        # Tweet

        try:
            self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div').send_keys(tweet)
        except NoSuchElementException:
            self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input').send_keys("internetspeedb6")
            self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input').send_keys(TWITTER_PASSWORD)
            self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div').click()

            time.sleep(5)
            self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div').send_keys(tweet)
        else:

            time.sleep(5)
            self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]/div').click()
        finally:
            time.sleep(5)

            self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]/div').click()
            print("Your complaint to your internet service provider was sent.")





