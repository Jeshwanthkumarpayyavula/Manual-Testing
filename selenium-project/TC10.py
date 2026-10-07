from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Launch Chrome
driver = webdriver.Chrome()
driver.maximize_window()

# Open JavaScript Alerts page
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

# Click the JS Alert button
driver.find_element(
    By.XPATH,
    "//button[text()='Click for JS Alert']"
).click()

# Create Explicit Wait
wait = WebDriverWait(driver, 10)

# Wait until the alert is present
alert = wait.until(EC.alert_is_present())

# Print alert text
print("Alert Text:", alert.text)

# Accept the alert
alert.accept()

# Verify the result
result = driver.find_element(By.ID, "result")

print("Result:", result.text)

time.sleep(5)

driver.quit()