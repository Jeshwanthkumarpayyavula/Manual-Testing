from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Launch Chrome
driver = webdriver.Chrome()
driver.maximize_window()

# Open website
driver.get("https://the-internet.herokuapp.com/hovers")

# Find the first user image
image = driver.find_element(By.XPATH, "(//div[@class='figure'])[1]")

# Create ActionChains object
actions = ActionChains(driver)

# Hover the mouse over the image
actions.move_to_element(image).perform()

time.sleep(2)

# Verify that the profile link appears
profile = driver.find_element(By.LINK_TEXT, "View profile")

if profile.is_displayed():
    print("Mouse Hover Successful")
else:
    print("Mouse Hover Failed")

time.sleep(5)
driver.quit()