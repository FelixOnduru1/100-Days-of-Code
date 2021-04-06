from selenium import webdriver
PYTHON_URL = "https://www.python.org/"

chrome_driver_path = "C:/Users/WORLDCOLE/Documents/DEVELOPMENT/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url=PYTHON_URL)

event_times = driver.find_elements_by_css_selector(".event-widget time")
event_names = driver.find_elements_by_css_selector(".event-widget .shrubbery .menu li a")
events = {}

for n in range(len(event_times)):
    events[n] = {"time": event_times[n].text,
                 "event": event_names[n].text}

print(events)
driver.quit()
