from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/javascript_alerts")

# Click "Click for JS Confirm"
driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()

# Switch to alert
alert = driver.switch_to.alert

print("Alert Text:", alert.text)

# Click Cancel
alert.dismiss()

# Verify result
result = driver.find_element(By.ID, "result")
print(result.text)

time.sleep(5)
driver.quit()