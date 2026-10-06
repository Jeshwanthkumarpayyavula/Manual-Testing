from selenium import webdriver

driver=webdriver.Chrome()
driver.get("https://www.flipkart.com/")
print(driver.title)
print(driver.current_url)
driver.maximize_window()
driver.refresh()
driver.back()
driver.forward()
driver.refresh()
driver.close()
driver.quit()
