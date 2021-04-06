from selenium import webdriver
from selenium.webdriver.common.keys import Keys

FIRST_NAME = "worldcole"
LAST_NAME = "worldcole"
EMAIL = "pythonsmtp404@gmail.com"

chrome_driver_path = "C:/Users/WORLDCOLE/Documents/DEVELOPMENT/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url="http://secure-retreat-92358.herokuapp.com/")
first_name_input = driver.find_element_by_name("fName")
first_name_input.send_keys(FIRST_NAME)

last_name_input = driver.find_element_by_name("lName")
last_name_input.send_keys(LAST_NAME)

email_input = driver.find_element_by_name("email")
email_input.send_keys(EMAIL)

submit_button = driver.find_element_by_css_selector("button")
submit_button.click()


