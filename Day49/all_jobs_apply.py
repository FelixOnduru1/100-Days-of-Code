from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import os
import time

EMAIl = os.environ["EMAIL"]
LINKEDIN_PASSWORD = os.environ["LINKEDIN_PASSWORD"]
LINKEDIN_URL = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=103644278&keywords=python%20developer&location=United%20States"
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

job_cards = driver.find_elements_by_class_name("job-card-container--clickable")

for job_card in job_cards:
    job_card.click()

    time.sleep(10)

    try:
        apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
        apply_button.click()

        phone_number = driver.find_element_by_css_selector(".fb-single-line-text input")
        if phone_number.text == "":
            phone_number.send_keys("0741237900")

        next_button = driver.find_element_by_css_selector("footer button")
        next_button.click()

        review_button = driver.find_elements_by_css_selector("footer button")[1]

        if review_button.get_attribute("data-control-name") == "continue_unify":
            print("This job has a further process. Therefore, the bot will skip it")
            dismiss_job = driver.find_element_by_css_selector(".artdeco-modal__dismiss path")
            dismiss_job.click()

            discard = driver.find_elements_by_css_selector(".artdeco-modal__actionbar button")[1]
            discard.click()

            print("Complex application skipped.")
            continue
        else:
            review_button.click()
            print("Job application successful.")

            submit_button = driver.find_elements_by_css_selector("footer button")[1]
            submit_button.click()

            time.sleep(5)
            dismiss_job = driver.find_element_by_css_selector(".artdeco-modal__dismiss path")
            dismiss_job.click()
            print("Job application successful.")
            continue

    except NoSuchElementException:
        print("No application button. Maybe job has been applied for in the past. Job skipped.")
        continue


driver.quit()
