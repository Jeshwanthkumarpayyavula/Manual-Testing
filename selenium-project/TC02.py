from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/javascript_alerts")

# Click the JS Alert button
driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()

# Switch to alert
alert = driver.switch_to.alert

print("Alert Text:", alert.text)

# Accept alert
alert.accept()

print("Alert Accepted Successfully")

time.sleep(10)

driver.quit()