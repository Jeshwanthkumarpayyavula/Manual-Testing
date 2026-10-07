from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Launch Chrome
driver = webdriver.Chrome()
driver.maximize_window()

# Open DemoQA Buttons page
driver.get("https://demoqa.com/buttons")

time.sleep(2)

# Locate Double Click button
double_click_btn = driver.find_element(By.ID, "doubleClickBtn")

# Create ActionChains object
actions = ActionChains(driver)

# Perform double click
actions.double_click(double_click_btn).perform()

time.sleep(2)

# Verify success message
message = driver.find_element(By.ID, "doubleClickMessage")

print("Result:", message.text)

time.sleep(5)

driver.quit()