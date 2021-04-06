from selenium import webdriver

chrome_driver_path = "C:/Users/WORLDCOLE/Documents/DEVELOPMENT/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url="https://www.amazon.com/Canon-RF50mm-Mirrorless-Cameras-4515C002/dp/B08MFVH7SV/ref=sr_1_14?dchild=1&keywords=canon+lens&qid=1617683771&sr=8-14")
price = driver.find_element_by_id("priceblock_ourprice")
print(price.text)

driver.quit()
