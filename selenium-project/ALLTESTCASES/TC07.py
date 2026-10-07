from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Launch Chrome
driver = webdriver.Chrome()
driver.maximize_window()

# Open Drag and Drop page
driver.get("https://the-internet.herokuapp.com/drag_and_drop")

time.sleep(2)

# Locate source and target elements
source = driver.find_element(By.ID, "column-a")
target = driver.find_element(By.ID, "column-b")

# Perform drag and drop
actions = ActionChains(driver)
actions.drag_and_drop(source, target).perform()

time.sleep(2)

# Verify drag and drop
header1 = driver.find_element(By.XPATH, '//*[@id="column-a"]/header').text
header2 = driver.find_element(By.XPATH, '//*[@id="column-b"]/header').text

print("Column A:", header1)
print("Column B:", header2)

print("Drag and Drop Performed Successfully")

time.sleep(5)
driver.quit()