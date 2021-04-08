from selenium import webdriver
import time


class InternetSpeedBot:
    def __init__(self, driver_path):

        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.down = 2
        self.up = 0.1

    def get_internet_speed(self):

        self.driver.get("https://www.speedtest.net/")
        self.driver.find_element_by_class_name("start-text").click()
        time.sleep(120)
        self.down = self.driver.find_element_by_class_name("download-speed").text
        self.up = self.driver.find_element_by_class_name("upload-speed").text

