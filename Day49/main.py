from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time

EMAIl = os.environ["EMAIL"]
LINKEDIN_PASSWORD = os.environ["LINKEDIN_PASSWORD"]
LINKEDIN_URL = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"
chrome_driver_path = "C:/Users/WORLDCOLE/Documents/DEVELOPMENT/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(url=LINKEDIN_URL)

sign_in = driver.find_element_by_link_text("Sign in")
sign_in.click()

email_sign_in = driver.find_element_by_id("username")
email_sign_in.send_keys(EMAIl)
password_sign_in = driver.find_element_by_id("password")
password_sign_in.send_keys(LINKEDIN_PASSWORD)

sign_in_page_link = driver.find_element_by_css_selector(".login__form_action_container  button")
sign_in_page_link.click()
time.sleep(10)

job_card = driver.find_element_by_class_name("job-card-container")
job_card.click()

time.sleep(10)
apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
apply_button.click()

phone_number = driver.find_element_by_css_selector(".fb-single-line-text input")
phone_number.send_keys("0741237900")

next_button = driver.find_element_by_css_selector("footer button")
next_button.click()

review_button = driver.find_elements_by_css_selector("footer button")[1]
review_button.click()

submit_button = driver.find_elements_by_css_selector("footer button")[1]
submit_button.click()
