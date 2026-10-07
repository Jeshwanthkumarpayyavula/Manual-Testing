from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch Chrome
driver = webdriver.Chrome()
driver.maximize_window()

# Open website
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

# Click the JS Prompt button
driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()

# Switch to the alert
alert = driver.switch_to.alert

# Print alert message
print("Alert Text:", alert.text)

# Enter text into the prompt
alert.send_keys("Jeshwanth Kumar")

# Click OK
alert.accept()

# Verify the result
result = driver.find_element(By.ID, "result")
print("Result:", result.text)

time.sleep(5)

driver.quit()