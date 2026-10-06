from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

driver.find_element(By.NAME, "my-text").send_keys("Python Selenium")
driver.find_element(By.NAME, "my-password").send_keys("Password123")
driver.find_element(By.NAME, "my-textarea").send_keys("John")
driver.find_element(By.NAME, "my-textarea").clear()
driver.find_element(By.NAME, "my-textarea").send_keys("Learning Selenium")

checkbox = driver.find_element(By.ID, "my-check-2")
if not checkbox.is_selected():
    checkbox.click()

radio = driver.find_element(By.ID, "my-radio-2")
if not radio.is_selected():
    radio.click()

country = Select(driver.find_element(By.NAME, "my-select"))
country.select_by_visible_text("Two")
# also demonstrate selecting by value/index
country.select_by_value("3")
country.select_by_index(1)

for option in country.options:
    print(option.text)

driver.quit()