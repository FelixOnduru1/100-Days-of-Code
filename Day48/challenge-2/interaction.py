from selenium import webdriver

chrome_driver_path = "C:/Users/WORLDCOLE/Documents/DEVELOPMENT/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url="https://en.wikipedia.org/wiki/Main_Page")
article_count = driver.find_element_by_css_selector("#articlecount a")
article_count_string = article_count.text
article_count_int = int(article_count_string.replace(",", ""))

print(article_count_int)

driver.quit()
